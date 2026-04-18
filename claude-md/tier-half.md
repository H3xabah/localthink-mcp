## Localthink — Half (file reads + execution tools)

### Token firewall — apply automatically
- Files >5KB (reading for info): `local_answer(file, question)` — never Read
- Logs: `local_compress_log(file)`
- Stack traces >10 lines: `local_compress_stack_trace(text)`
- JSON/CSV/API >2KB: `local_compress_data(data)`
- Command output: `local_gate(raw_output)` → `local_slice(file, offset)` on demand
- Exception/error: `local_explain_error(error_text, file_path?)`

### Code navigation
1. `local_symbols(file)` — symbol table + line numbers
2. `local_find_impl(file, "spec")` — jump to implementation
3. `local_strip_to_skeleton(file)` — structure without bodies
4. `local_code_surface(file)` — public API (Python: AST, instant)
5. Read directly only when: editing or file <5KB

### Multi-file
- `local_batch_answer([f1, f2], question)` — never loop Read
- `local_scan_dir(dir, "*.py")` — concurrent, none enter context
- `local_diff_files(a, b)` / `local_git_diff(repo?, ref?)` — diff without loading

### Execution filters
- `local_run_tests()` → `{failed, delta, pointer}` only
- `local_run_lint()` → violations by rule, passing suppressed
- `local_run_build()` → root cause + symbols only

### Session scratchpad
- `local_memo_write("decisions"|"pitfalls", content)` — write as you go
- `local_memo_read()` — distilled summary
- `local_memo_checkpoint()` → RESUME_PROMPT for /clear

### When unsure
`local_suggest(task, files?)` → ordered call plan
`local_auto(input, question?)` → auto-selects the right operation

### Do not offload
Files <5KB · Files you are about to Edit · Binary files
