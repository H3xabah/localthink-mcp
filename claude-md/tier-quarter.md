## Localthink — Quarter Mode (token-saving essentials only)

Apply automatically — no prompting needed:

- **Files >5KB** (reading for info): `local_answer(file, question)` — never Read
- **Log files** (`*.log`, large `*.txt`): `local_compress_log(file)`
- **Stack traces >10 lines**: `local_compress_stack_trace(text)`
- **JSON/CSV/API payloads >2KB**: `local_compress_data(data)`
- **Command/build output**: `local_gate(raw_output)` before it enters context
- **After gate signals anomaly**: `local_slice(file, offset_lines)` for the raw window

Do NOT use `Read` for large files — route through localthink first.
Files <5KB and files you are about to `Edit`: use `Read` directly.
