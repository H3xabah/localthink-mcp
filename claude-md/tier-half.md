## Localthink — Half Mode (file reads + execution tools)

### Token Firewall — Apply automatically
- **Files >5KB** (reading for info): `local_answer(file, question)` — never Read
- **Logs**: `local_compress_log(file)`
- **Stack traces >10 lines**: `local_compress_stack_trace(text)`
- **JSON/CSV/API >2KB**: `local_compress_data(data)`
- **Command output**: `local_gate(raw_output)` → `local_slice(file, offset)` on demand

### Code Navigation
1. `local_symbols(file)` — symbol table + line numbers
2. `local_find_impl(file, "spec")` — jump to implementation
3. `local_strip_to_skeleton(file)` — structure without bodies
4. `local_code_surface(file)` — public API (Python: AST, instant)
5. **Read directly only when:** editing or file <5KB

### Multi-file
- `local_batch_answer([f1, f2], question)` — never loop Read
- `local_scan_dir(dir, "*.py")` — concurrent, none enter context
- `local_diff_files(a, b)` — diff without loading either file

### Execution Filters
- `local_run_tests()` → `{failed, delta, pointer}` only
- `local_run_lint()` → violations by rule, passing suppressed
- `local_run_build()` → root cause + symbols only

### Session Scratchpad
- `local_memo_write("decisions"|"pitfalls", content)` — write as you go
- `local_memo_read()` — distilled summary
- `local_memo_checkpoint()` → RESUME_PROMPT for `/clear`

### When Unsure
`local_auto(input, question)` — auto-selects the right operation

### What NOT to Offload
Files <5KB · Files you are about to `Edit` · Binary files / images
