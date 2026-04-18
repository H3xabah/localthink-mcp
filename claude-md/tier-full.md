## Localthink — Full (49 tools)

### First call — always
Before any non-trivial task, call:
```
local_suggest(task, files?)
```
Returns an ordered call plan. No reasoning overhead. Skip only for trivial one-liners.

### Token firewall — apply automatically
| Content | Use instead |
|---------|-------------|
| File >5KB (reading for info) | `local_answer(file, question)` |
| Log files / large .txt | `local_compress_log(file)` |
| Stack trace >10 lines | `local_compress_stack_trace(text)` |
| JSON/CSV/API payload >2KB | `local_compress_data(data)` |
| Command/build/test output | `local_gate(raw_output)` → `local_slice(file, offset)` on demand |
| Conversation transcript | `local_session_compress(file)` |
| CLAUDE.md / system prompt | `local_prompt_compress(text)` |
| Vague prompt | `local_improve_prompt(prompt, context?)` |
| Large or complex task | `local_preplan(task, context?, depth?)` |
| Exception / error | `local_explain_error(error_text, file_path?)` |

### Code navigation
1. `local_symbols(file)` — full symbol table with line numbers
2. `local_find_impl(file, "plain English spec")` — jump to implementation
3. `local_strip_to_skeleton(file)` — structure without bodies
4. `local_code_surface(file)` — public API (Python: AST, instant; other: fast LLM)
5. Read directly only when: about to Edit, or file <5KB

### Multi-file
- `local_batch_answer([f1, f2, ...], question)` — never loop Read
- `local_scan_dir(dir, "*.py")` — concurrent scan, none enter context
- `local_diff_files(a, b)` / `local_git_diff(repo?, ref?)` — diff without loading

### Smart buffer
1. `local_gate(raw_output)` → Pattern + Anomalies + Signal (TINY, instant)
2. `local_slice(file, offset)` — raw window on demand after gate signals anomaly
3. `local_diff_semantic(before, after)` — logic/API/security changes only

### Execution filters
- `local_run_tests()` → `{failed, delta, pointer}` only (new failures auto-saved to pitfalls)
- `local_run_lint()` → violations by rule, passing rules suppressed
- `local_run_build()` → root cause + affected symbols only

### Documents & data
- `local_shrink_file(file)` — compressed doc for repeated reference
- `local_outline(text)` → `local_extract(text, query)` for targeted sections
- `local_chat(doc, q, history?)` — multi-turn Q&A, doc never enters context
- `local_pipeline(text, steps)` — chain ops in one call (steps are cached individually)
- `local_translate(text, "yaml")` · `local_schema_infer(data)` · `local_timeline(text)`

### Session & memory
- `local_session_recall(task)` — call at session start; surfaces notes + last checkpoint
- `local_memo_write("decisions"|"pitfalls"|"open_questions"|"assumptions", content)`
- `local_memo_read()` — distilled summary · `local_memo_checkpoint()` → RESUME_PROMPT
- `local_note_write("gotcha"|"pattern"|"architecture", content)` — permanent, cross-session
- `local_note_search(query)` — keyword/embedding search across all notes

### Config
- `local_config()` — settings GUI (Ollama, Timeouts, Limits, Cache, Memo tabs)
- `local_models()` — show MAIN/FAST/TINY tiers + Ollama health

### Do not offload
Files <5KB · Files you are about to Edit · Current CLAUDE.md / task spec · Binary files
