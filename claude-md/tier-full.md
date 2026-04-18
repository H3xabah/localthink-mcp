## Localthink — Full Mode (all tools active)

### Token Firewall
| Content | Use instead |
|---------|-------------|
| File >5KB (reading for info) | `local_answer(file, question)` |
| Log files (`*.log`, large `*.txt`) | `local_compress_log(file)` |
| Stack traces >10 lines | `local_compress_stack_trace(text)` |
| JSON/CSV/API payloads >2KB | `local_compress_data(data)` |
| Command/build/test output | `local_gate(raw_output)` → `local_slice(file, offset)` on demand |
| Conversation transcript | `local_session_compress(file)` |
| CLAUDE.md / system prompt | `local_prompt_compress(text)` |
| Vague user prompt | `local_improve_prompt(prompt, context?)` |
| Large or complex task | `local_preplan(task, context?, depth?)` |

### Code Navigation
1. `local_symbols(file)` — full symbol table with line numbers
2. `local_find_impl(file, "plain English spec")` — jump to implementation
3. `local_strip_to_skeleton(file)` — structure without bodies
4. `local_code_surface(file)` — public API (Python: pure AST, instant)
5. **Read directly only when:** about to Edit (need exact lines) or file <5KB

### Multi-file
- `local_batch_answer([f1, f2, ...], question)` — never loop Read
- `local_scan_dir(dir, "*.py")` — concurrent scan, none enter context
- `local_route(dir, intent, "**/*.ts")` — intent → ranked relevant files
- `local_diff_files(a, b)` — neither file enters context

### Smart Buffer
1. `local_gate(raw_output)` → Pattern + Anomalies + Signal (TINY model, instant)
2. `local_slice(file, offset)` — raw window, only on demand after gate signals anomaly
3. `local_diff_semantic(before, after)` — logic/API/security changes only, noise suppressed

### Execution Filters
- `local_run_tests()` → `{failed, delta, pointer}` — raw output never enters context
- `local_run_lint()` → violations by rule, passing rules suppressed
- `local_run_build()` → root cause + affected symbols only

### Documents & Data
- `local_shrink_file(file)` — compressed whole doc for repeated reference
- `local_outline(text)` → `local_extract(text, query)` for targeted sections
- `local_chat(doc, q, history)` — multi-turn Q&A, doc never enters context
- `local_pipeline(text, steps)` — chain ops: summarize → extract → answer → refine
- `local_translate(text, "yaml")`, `local_schema_infer(data)`, `local_timeline(text)`

### Session Scratchpad
- `local_memo_write("decisions"|"pitfalls"|"open_questions", content)` — write as you go
- `local_memo_read()` — distilled summary
- `local_memo_checkpoint()` → RESUME_PROMPT, paste after `/clear`

### Permanent Notes
- `local_note_write("gotcha"|"pattern"|"architecture", content)` — cross-session
- `local_note_search(query)` — call at session start for relevant prior knowledge

### Navigation & Safety
- `local_hallucination_check(dir, ["name1", "name2"])` — verify names exist (instant, no LLM)
- `local_classify(text)` — unknown content → tool recommendation
- `local_audit(file, checklist)` — checklist pass/fail, file never enters context

### Config
- `local_config()` — settings GUI (models, timeouts, cache, memo dirs)
- `local_models()` — show MAIN/FAST/TINY tiers + current config

### What NOT to Offload
Files <5KB · Files you are about to `Edit` · Current CLAUDE.md / task spec · Binary files / images
