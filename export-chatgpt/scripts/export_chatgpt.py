#!/usr/bin/env python3
"""Export a ChatGPT shared conversation to Markdown or JSON.

Usage:
  export_chatgpt.py <chatgpt share url> [--format md|json|both] [--out PATH] [--roles user,assistant]
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timezone
from typing import Any, Dict, List

USER_AGENT = "chatgpt-to-md/0.1 (+https://chatgpt.com)"
STREAM_MARKER = 'streamController.enqueue("'


def fetch_html(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = resp.read()
    return data.decode("utf-8", errors="replace")


def extract_stream_payload(html: str) -> str:
    start = html.find(STREAM_MARKER)
    if start == -1:
        raise ValueError("Unable to find streamController.enqueue payload. The page format may have changed.")
    i = start + len(STREAM_MARKER)
    buf: List[str] = []
    while i < len(html):
        c = html[i]
        if c == "\"":
            # A quote ends the string unless it is escaped by an odd number of backslashes.
            backslashes = 0
            j = i - 1
            while j >= 0 and html[j] == "\\":
                backslashes += 1
                j -= 1
            if backslashes % 2 == 0:
                break
        buf.append(c)
        i += 1
    if i >= len(html):
        raise ValueError("Unable to parse streamController.enqueue payload.")
    chunk = "".join(buf)
    return json.loads("\"" + chunk + "\"")


def decode_stream_payload(payload: str) -> List[Any]:
    return json.loads(payload)


def decode_node(arr: List[Any], node: Any, memo: Dict[int, Any], visiting: set) -> Any:
    if isinstance(node, int):
        if node == -5:
            return None
        if node < 0 or node >= len(arr):
            return node
        if node in memo:
            return memo[node]
        if node in visiting:
            return {"__ref__": node}
        visiting.add(node)
        value = decode_node(arr, arr[node], memo, visiting)
        memo[node] = value
        visiting.remove(node)
        return value
    if isinstance(node, list):
        return [decode_node(arr, item, memo, visiting) for item in node]
    if isinstance(node, dict) and all(
        isinstance(k, str) and k.startswith("_") and k[1:].isdigit() for k in node.keys()
    ):
        out: Dict[Any, Any] = {}
        for k, v in node.items():
            key = decode_node(arr, int(k[1:]), memo, visiting)
            out[key] = decode_node(arr, v, memo, visiting)
        return out
    if isinstance(node, dict):
        return {k: decode_node(arr, v, memo, visiting) for k, v in node.items()}
    return node


def extract_server_response(arr: List[Any]) -> Dict[str, Any]:
    try:
        idx = arr.index("serverResponse")
    except ValueError as exc:
        raise ValueError("serverResponse not found in payload.") from exc
    memo: Dict[int, Any] = {}
    visiting: set = set()
    return decode_node(arr, arr[idx + 1], memo, visiting)


def extract_messages(mapping: Dict[str, Any]) -> List[Dict[str, Any]]:
    roots = [mid for mid, entry in mapping.items() if entry.get("parent") is None]
    ordered: List[Dict[str, Any]] = []
    seen: set = set()

    def traverse(node_id: str) -> None:
        if node_id in seen:
            return
        seen.add(node_id)
        entry = mapping.get(node_id)
        if not entry:
            return
        msg = entry.get("message")
        if msg:
            ordered.append(msg)
        for child_id in entry.get("children") or []:
            traverse(child_id)

    for root_id in roots:
        root_entry = mapping.get(root_id, {})
        children = root_entry.get("children") or []
        if children:
            for child_id in children:
                traverse(child_id)
        else:
            traverse(root_id)

    return ordered


def normalize_messages(messages: List[Dict[str, Any]], roles_filter: List[str] | None) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for msg in messages:
        role = (msg.get("author") or {}).get("role") or "unknown"
        if roles_filter and role not in roles_filter:
            continue
        content_obj = msg.get("content") or {}
        parts = content_obj.get("parts") or []
        text_parts = [p for p in parts if isinstance(p, str)]
        content = "\n".join(text_parts).strip()
        out.append(
            {
                "id": msg.get("id"),
                "role": role,
                "content": content,
                "content_type": content_obj.get("content_type"),
                "status": msg.get("status"),
            }
        )
    return out


def compute_fence(text: str) -> str:
    matches = re.findall(r"`+", text)
    max_len = max((len(m) for m in matches), default=0)
    return "`" * max(3, max_len + 1)


def render_markdown(title: str, url: str, messages: List[Dict[str, Any]]) -> str:
    exported_at = datetime.now(timezone.utc).isoformat()
    lines: List[str] = []
    if title:
        lines.append(f"# {title}")
    else:
        lines.append("# ChatGPT Export")
    lines.append(f"Source: {url}")
    lines.append(f"Exported: {exported_at}")
    lines.append("")

    for msg in messages:
        lines.append("---")
        lines.append(f"role: {msg['role']}")
        if msg.get("id"):
            lines.append(f"id: {msg['id']}")
        fence = compute_fence(msg.get("content", ""))
        lines.append(f"{fence}text")
        lines.append(msg.get("content", ""))
        lines.append(fence)
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render_json(title: str, url: str, messages: List[Dict[str, Any]]) -> str:
    exported_at = datetime.now(timezone.utc).isoformat()
    payload = {
        "title": title,
        "source_url": url,
        "exported_at": exported_at,
        "messages": messages,
    }
    return json.dumps(payload, indent=2, ensure_ascii=True) + "\n"


def parse_roles(roles: str | None) -> List[str] | None:
    if not roles:
        return None
    return [r.strip() for r in roles.split(",") if r.strip()]


def write_output(path: str | None, content: str) -> None:
    if not path:
        sys.stdout.write(content)
        return
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def main() -> int:
    parser = argparse.ArgumentParser(description="Export a ChatGPT shared conversation.")
    parser.add_argument("url", help="ChatGPT share URL (https://chatgpt.com/share/...)" )
    parser.add_argument("--format", choices=["md", "json", "both"], default="md")
    parser.add_argument("--out", help="Output path (file for md/json, base path for both)")
    parser.add_argument("--roles", help="Comma-separated roles to include (e.g. user,assistant)")

    args = parser.parse_args()
    roles_filter = parse_roles(args.roles)

    html = fetch_html(args.url)
    payload = extract_stream_payload(html)
    arr = decode_stream_payload(payload)
    server = extract_server_response(arr)
    data = server.get("data") if isinstance(server, dict) else None
    if not data:
        raise ValueError("Unexpected serverResponse format.")
    mapping = data.get("mapping") or {}
    title = data.get("title") or ""

    messages = extract_messages(mapping)
    normalized = normalize_messages(messages, roles_filter)

    if args.format == "md":
        output = render_markdown(title, args.url, normalized)
        write_output(args.out, output)
        return 0
    if args.format == "json":
        output = render_json(title, args.url, normalized)
        write_output(args.out, output)
        return 0

    # both
    if not args.out:
        raise ValueError("--out is required when --format=both")
    base, ext = os.path.splitext(args.out)
    if ext in (".md", ".json"):
        base = base
    else:
        base = args.out
    write_output(base + ".md", render_markdown(title, args.url, normalized))
    write_output(base + ".json", render_json(title, args.url, normalized))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # pragma: no cover
        sys.stderr.write(f"Error: {exc}\n")
        sys.exit(1)
