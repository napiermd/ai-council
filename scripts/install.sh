#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
BIN_DIR="${HOME}/.local/bin"
CLAUDE_DIR="${HOME}/.claude/commands"
CODEX_DIR_UPPER="${HOME}/.Codex/commands"
CODEX_DIR_LOWER="${HOME}/.codex/commands"

shell_name="${SHELL##*/}"
case "$shell_name" in
  zsh) shell_rc="${HOME}/.zshrc" ;;
  bash) shell_rc="${HOME}/.bashrc" ;;
  *) shell_rc="${HOME}/.profile" ;;
esac

mkdir -p "$BIN_DIR" "$CLAUDE_DIR" "$CODEX_DIR_UPPER" "$CODEX_DIR_LOWER"
ln -sfn "$REPO_ROOT/bin/ai-council" "$BIN_DIR/ai-council"

path_line='export PATH="$HOME/.local/bin:$PATH"'
if [ -f "$shell_rc" ]; then
  if ! grep -Fq "$path_line" "$shell_rc"; then
    printf '\n# AI Council CLI\n%s\n' "$path_line" >> "$shell_rc"
  fi
else
  printf '# AI Council CLI\n%s\n' "$path_line" > "$shell_rc"
fi

find "$REPO_ROOT/commands/claude" -maxdepth 1 -type f -name "*.md" -print | while read -r file; do
  cp "$file" "$CLAUDE_DIR/$(basename "$file")"
done

find "$REPO_ROOT/commands/codex" -maxdepth 1 -type f -name "*.md" -print | while read -r file; do
  cp "$file" "$CODEX_DIR_UPPER/$(basename "$file")"
  cp "$file" "$CODEX_DIR_LOWER/$(basename "$file")"
done

cat <<EOF
Installed AI Council.

Binary:
  $BIN_DIR/ai-council

Shell startup file:
  $shell_rc

Claude commands:
  $CLAUDE_DIR

Codex commands:
  $CODEX_DIR_UPPER
  $CODEX_DIR_LOWER

Open a new shell, then try:
  ai-council doctor
  ai-council list commands
  ai-council prompt systems "Should this agent stack keep a planner?"
EOF
