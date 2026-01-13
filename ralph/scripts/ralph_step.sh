#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage:
  ralph_step.sh --index <n> --count <total> --prompt "<task>" [--run-id <id>] [--context-file <path>] [--out-dir <dir>] [--run|--dry-run]

Options:
  --index         1-based loop index
  --count         total number of loops
  --prompt        original task prompt (required)
  --run-id        unique run identifier (default: timestamp+pid+random)
  --context-file  path to a file containing loop context (optional)
  --out-dir       output directory for prompt/output files (default: .ralph)
  --run           execute codex exec (default is dry-run)
  --dry-run       generate prompt file only
  -h, --help      show this help

Exit codes:
  0  success
  2  RALPH_STOP detected in subprocess output
USAGE
}

index=""
count=""
prompt=""
run_id=""
context_file=""
out_dir=".ralph"
run_mode="dry"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --index)
      index="$2"; shift 2 ;;
    --count)
      count="$2"; shift 2 ;;
    --prompt)
      prompt="$2"; shift 2 ;;
    --run-id)
      run_id="$2"; shift 2 ;;
    --context-file)
      context_file="$2"; shift 2 ;;
    --out-dir)
      out_dir="$2"; shift 2 ;;
    --run)
      run_mode="run"; shift ;;
    --dry-run)
      run_mode="dry"; shift ;;
    -h|--help)
      usage; exit 0 ;;
    *)
      echo "Unknown argument: $1" >&2
      usage
      exit 1
      ;;
  esac
done

if [[ -z "$index" || -z "$count" || -z "$prompt" ]]; then
  echo "Missing required arguments." >&2
  usage
  exit 1
fi

if ! [[ "$index" =~ ^[0-9]+$ ]] || ! [[ "$count" =~ ^[0-9]+$ ]]; then
  echo "--index and --count must be positive integers." >&2
  exit 1
fi

if [[ "$index" -lt 1 || "$count" -lt 1 ]]; then
  echo "--index and --count must be >= 1." >&2
  exit 1
fi

if [[ -z "$run_id" ]]; then
  run_id="$(date +%Y%m%d-%H%M%S)-$$-$RANDOM"
fi

run_dir="$out_dir/$run_id"
mkdir -p "$run_dir"

if [[ -z "$context_file" ]]; then
  context_file="$run_dir/context.txt"
fi

loop_context="(none)"
if [[ -f "$context_file" ]]; then
  loop_context="$(cat "$context_file")"
fi

prompt_file="$run_dir/prompt-$index.txt"
output_file="$run_dir/output-$index.txt"

cat <<PROMPT_EOF > "$prompt_file"
You are subprocess #$index of $count in a Ralph loop.
Original request:
$prompt

Loop context so far:
$loop_context

Do the work requested. Provide:
- DETAILED_WORKLOG: Describe what you checked and why.
- FINDINGS: Bugs, risks, or concerns.
- RECOMMENDATIONS: Concrete fixes or next steps.
- CONTROLLER_NOTES: A concise summary for the next loop.
- STOP: "NO" or "RALPH_STOP: <reason>" if critical and not recoverable.
PROMPT_EOF

if [[ "$run_mode" == "dry" ]]; then
  echo "Dry run: wrote $prompt_file"
  echo "Run id: $run_id"
  echo "Context file: $context_file"
  echo "To run: printf '%s\\n' \"\$(cat $prompt_file)\" | codex exec > $output_file"
  exit 0
fi

printf '%s\n' "$(cat "$prompt_file")" | codex exec > "$output_file"

if grep -q "RALPH_STOP" "$output_file"; then
  echo "RALPH_STOP detected in $output_file" >&2
  exit 2
fi

echo "Wrote $output_file"
