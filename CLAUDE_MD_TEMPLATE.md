# Localthink CLAUDE.md — Tiered Instruction System

Localthink ships three instruction tiers. Pick one based on how aggressively you want
Claude to offload work to the local model. The `set-tier.py` switcher injects the chosen
tier's content directly into your `CLAUDE.md` — no imports, no extra files at runtime.

---

## Quick Start

```bash
# Copy the claude-md/ directory somewhere accessible (e.g. ~/.claude/localthink/)
cp -r claude-md/ ~/.claude/localthink/

# Check current tier (none set yet)
python ~/.claude/localthink/set-tier.py

# Set your tier
python ~/.claude/localthink/set-tier.py full     # all 45 tools (~55 lines)
python ~/.claude/localthink/set-tier.py half     # file reads + execution (~30 lines)
python ~/.claude/localthink/set-tier.py quarter  # token-saving only (~12 lines)
```

`set-tier.py` writes directly into `~/.claude/CLAUDE.md`, wrapping the block in HTML
comment bookmarks so it can be swapped again later without touching anything else.

---

## Tier Comparison

| Tier | Lines in CLAUDE.md | Tools active | Best for |
|------|-------------------|--------------|----------|
| **full** | ~55 | All 45 | Complex projects, new codebases, research-heavy sessions |
| **half** | ~30 | ~18 | Day-to-day dev: file nav + CI/test filters |
| **quarter** | ~12 | ~6 | Minimal overhead — just stop Claude loading big files |

All tiers are a reduction vs the old monolithic template (102 lines). Even `full` is 46% smaller.

---

## Tier Contents

### quarter (~12 lines) — Token Firewall Only

```
local_answer         files >5KB instead of Read
local_compress_log   log files
local_compress_stack_trace   stack traces >10 lines
local_compress_data  JSON/CSV/API payloads >2KB
local_gate           command/build output
local_slice          raw window on demand after gate
```

### half (~30 lines) — File Reads + Execution

Adds on top of quarter:
```
local_symbols        local_find_impl      local_strip_to_skeleton
local_code_surface   local_batch_answer   local_scan_dir
local_diff_files     local_run_tests      local_run_lint
local_run_build      local_memo_write     local_memo_read
local_memo_checkpoint  local_auto
```

### full (~55 lines) — All Tools

Adds on top of half:
```
local_route              local_hallucination_check
local_chat               local_pipeline
local_shrink_file        local_outline         local_extract
local_translate          local_schema_infer    local_timeline
local_improve_prompt     local_preplan         local_refine
local_diff_semantic      local_session_compress  local_prompt_compress
local_note_write         local_note_search
local_classify           local_audit
local_config             local_models
```

---

## Switching Tiers

```bash
# Switch at any time — safe to run multiple times
python ~/.claude/localthink/set-tier.py half

# Check what's active
python ~/.claude/localthink/set-tier.py
# Current tier : half
# Block size   : 30 lines in CLAUDE.md
```

The switcher uses HTML comment bookmarks (`<!-- localthink-tier-start/end -->`) to find
and replace only the managed block. Everything else in your `CLAUDE.md` is untouched.

---

## Tier Files

The three tier files live in `claude-md/`:

| File | Purpose |
|------|---------|
| `tier-full.md` | All 45 tools — every rule and use case |
| `tier-half.md` | File reads + execution filters |
| `tier-quarter.md` | Token-saving essentials only |
| `set-tier.py` | Switcher — edits CLAUDE.md in place |

---

## Notes

- **Threshold 5KB**: roughly 1,250 tokens. Below this, `Read` is cheaper than the MCP round-trip.
- **Python AST**: `local_code_surface` on `.py` files uses no Ollama — instant and deterministic.
- **`local_auto` as escape hatch**: when the right tool is unclear, it picks for you (half + full only).
- **Upgrading**: run `set-tier.py full` after updating localthink to pick up new tool rules automatically.
