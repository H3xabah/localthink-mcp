# Localthink CLAUDE.md — Tiered Instruction System

Three instruction tiers inject directly into CLAUDE.md via set-tier.py.
Pick the tier that matches how aggressively you want to offload to the local model.

## Quick start

```bash
# Copy the claude-md/ directory somewhere accessible
cp -r claude-md/ ~/.claude/localthink/      # macOS/Linux
xcopy claude-md\ %USERPROFILE%\.claude\localthink\ /E  # Windows

# Set your tier
python ~/.claude/localthink/set-tier.py full      # all 49 tools (~60 lines)
python ~/.claude/localthink/set-tier.py half      # file reads + execution (~35 lines)
python ~/.claude/localthink/set-tier.py quarter   # token-saving only (~15 lines)

# Check current tier
python ~/.claude/localthink/set-tier.py
```

set-tier.py writes into ~/.claude/CLAUDE.md using HTML comment bookmarks
(<!-- localthink-tier-start/end -->) to isolate the managed block.
Everything else in your CLAUDE.md is untouched.

## Tier comparison

| Tier    | Lines in CLAUDE.md | Tools | Best for |
|---------|--------------------|-------|----------|
| full    | ~60                | 49    | Complex projects, new codebases, research sessions |
| half    | ~35                | ~22   | Day-to-day dev: file nav + CI filters |
| quarter | ~15                | ~7    | Minimal — prevent large-file loads only |

## What each tier includes

### quarter (~15 lines) — Token firewall + debugging
local_answer · local_compress_log · local_compress_stack_trace · local_compress_data
local_gate · local_slice · local_explain_error

### half (~35 lines) — File reads + execution
Adds: local_symbols · local_find_impl · local_strip_to_skeleton · local_code_surface
local_batch_answer · local_scan_dir · local_diff_files · local_git_diff
local_run_tests · local_run_lint · local_run_build
local_memo_write · local_memo_read · local_memo_checkpoint
local_suggest · local_auto

### full (~60 lines) — All 49 tools
Adds: local_chat · local_pipeline · local_shrink_file · local_outline · local_extract
local_translate · local_schema_infer · local_timeline · local_diff_semantic
local_improve_prompt · local_preplan · local_refine · local_session_compress
local_prompt_compress · local_note_write · local_note_search · local_session_recall
local_classify · local_audit · local_grep_semantic · local_config · local_models

## Switching tiers

```bash
python ~/.claude/localthink/set-tier.py half   # switch
python ~/.claude/localthink/set-tier.py        # check current tier and block size
```

## Notes

- **5KB threshold** — ~1,250 tokens. Below this, Read is cheaper than the MCP round-trip.
- **Python AST** — local_code_surface on .py files uses no Ollama: instant, deterministic.
- **local_suggest** — when unsure which tool fits, it returns an ordered call plan (all tiers).
- **local_explain_error** — auto-detects the implicated file from the stack trace.
- **local_git_diff** — diffs HEAD vs working tree via the local LLM. Requires git in PATH.
- **local_session_recall** — call at session start to surface relevant notes + last checkpoint.
- **Upgrading** — run set-tier.py full after updating to pick up new tool rules automatically.
