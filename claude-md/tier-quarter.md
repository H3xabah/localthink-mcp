## Localthink — Quarter (token-saving essentials)

Apply automatically — no prompting needed:

- Files >5KB (reading for info): `local_answer(file, question)` — never Read
- Log files (*.log, large *.txt): `local_compress_log(file)`
- Stack traces >10 lines: `local_compress_stack_trace(text)`
- JSON/CSV/API payloads >2KB: `local_compress_data(data)`
- Command/build output: `local_gate(raw_output)` before it enters context
- Gate signals anomaly: `local_slice(file, offset_lines)` for the raw window
- Exception/error: `local_explain_error(error_text)` — root cause + fix, no file load

Do NOT use Read for large files. Files <5KB and files you are about to Edit: use Read directly.
