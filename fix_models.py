from pathlib import Path

p = Path("C:/Users/Aiden/code/localthink-mcp-2.2/SETUP.md")
text = p.read_text(encoding="utf-8")

replacements = [
    # Quick-start header (Tier E example): pull line
    (
        "ollama pull qwen2.5:3b                     # FAST + TINY",
        "ollama pull qwen2.5:7b-instruct-q4_K_M   # FAST\nollama pull qwen2.5:3b                     # TINY"
    ),
    # Quick-start macOS register (unique context: followed by "# 3.")
    (
        '  --env OLLAMA_FAST_MODEL="qwen2.5:3b" \\\n  --env OLLAMA_TINY_MODEL="qwen2.5:3b" \\\n  -- uvx localthink-mcp\n\n# 3.',
        '  --env OLLAMA_FAST_MODEL="qwen2.5:7b-instruct-q4_K_M" \\\n  --env OLLAMA_TINY_MODEL="qwen2.5:3b" \\\n  -- uvx localthink-mcp\n\n# 3.'
    ),
    # Quick-start Windows register (unique context: followed by "\n\nxcopy")
    (
        '  --env OLLAMA_FAST_MODEL="qwen2.5:3b" ^\n  --env OLLAMA_TINY_MODEL="qwen2.5:3b" ^\n  -- cmd /c uvx localthink-mcp\n\nxcopy',
        '  --env OLLAMA_FAST_MODEL="qwen2.5:7b-instruct-q4_K_M" ^\n  --env OLLAMA_TINY_MODEL="qwen2.5:3b" ^\n  -- cmd /c uvx localthink-mcp\n\nxcopy'
    ),
    # Header table: Row A
    (
        "| A | CPU · 16 GB RAM | `qwen2.5:7b-instruct-q4_K_M` | `qwen2.5:1.5b` | `qwen2.5:1.5b` | 3-8 |",
        "| A | CPU · 16 GB RAM | `qwen2.5:7b-instruct-q4_K_M` | `qwen2.5:3b` | `qwen2.5:1.5b` | 3-8 |"
    ),
    # Header table: Row A+
    (
        "| A+ | CPU · 32 GB RAM | `qwen2.5:14b-instruct-q4_K_M` | `qwen2.5:3b` | `qwen2.5:3b` | 2-5 |",
        "| A+ | CPU · 32 GB RAM | `qwen2.5:14b-instruct-q4_K_M` | `qwen2.5:7b-instruct-q4_K_M` | `qwen2.5:3b` | 2-5 |"
    ),
    # Header table: Row B
    (
        "| B | 4 GB VRAM | `qwen2.5:7b-instruct-q4_K_M` | `qwen2.5:1.5b` | `qwen2.5:1.5b` | 20-40 |",
        "| B | 4 GB VRAM | `qwen2.5:7b-instruct-q4_K_M` | `qwen2.5:3b` | `qwen2.5:1.5b` | 20-40 |"
    ),
    # Header table: Row C
    (
        "| C | 6 GB VRAM | `qwen2.5:7b-instruct-q6_K` | `qwen2.5:3b` | `qwen2.5:3b` | 25-45 |",
        "| C | 6 GB VRAM | `qwen2.5:7b-instruct-q6_K` | `qwen2.5:3b` | `qwen2.5:1.5b` | 25-45 |"
    ),
    # Header table: Row D
    (
        "| D | 8 GB VRAM | `qwen2.5:7b-instruct-q8_0` | `qwen2.5:3b` | `qwen2.5:3b` | 30-55 |",
        "| D | 8 GB VRAM | `qwen2.5:7b-instruct-q8_0` | `qwen2.5:3b` | `qwen2.5:1.5b` | 30-55 |"
    ),
    # Header table: Row E
    (
        "| E | 10-12 GB VRAM | `qwen2.5:14b-instruct-q4_K_M` | `qwen2.5:3b` | `qwen2.5:3b` | 20-40 |",
        "| E | 10-12 GB VRAM | `qwen2.5:14b-instruct-q4_K_M` | `qwen2.5:7b-instruct-q4_K_M` | `qwen2.5:3b` | 20-40 |"
    ),
    # Header table: Row G
    (
        "| G | 24 GB VRAM | `qwen2.5:32b-instruct-q4_K_M` | `qwen2.5:7b-instruct-q4_K_M` | `qwen2.5:3b` | 15-30 |",
        "| G | 24 GB VRAM | `qwen2.5:32b-instruct-q4_K_M` | `qwen2.5:7b-instruct-q8_0` | `qwen2.5:3b` | 15-30 |"
    ),
    # Header table: Apple 8GB
    (
        "| Apple M · 8 GB | M1/M2/M3 base | `qwen2.5:7b-instruct-q4_K_M` | `qwen2.5:1.5b` | `qwen2.5:1.5b` | 15-30 |",
        "| Apple M · 8 GB | M1/M2/M3 base | `qwen2.5:7b-instruct-q4_K_M` | `qwen2.5:3b` | `qwen2.5:1.5b` | 15-30 |"
    ),
    # Header table: Apple 16-24GB
    (
        "| Apple M · 16-24 GB | M Pro | `qwen2.5:14b-instruct-q4_K_M` | `qwen2.5:3b` | `qwen2.5:3b` | 20-45 |",
        "| Apple M · 16-24 GB | M Pro | `qwen2.5:14b-instruct-q4_K_M` | `qwen2.5:7b-instruct-q4_K_M` | `qwen2.5:3b` | 20-45 |"
    ),
    # Header table: Apple 32-40GB
    (
        "| Apple M · 32-40 GB | M Max | `qwen2.5:32b-instruct-q4_K_M` | `qwen2.5:7b-instruct-q4_K_M` | `qwen2.5:3b` | 15-30 |",
        "| Apple M · 32-40 GB | M Max | `qwen2.5:32b-instruct-q4_K_M` | `qwen2.5:7b-instruct-q8_0` | `qwen2.5:3b` | 15-30 |"
    ),
    # Step 3 Tier E example
    (
        "# Example: Tier E (10-12 GB VRAM)\nollama pull qwen2.5:14b-instruct-q4_K_M   # MAIN\nollama pull qwen2.5:3b                     # FAST + TINY",
        "# Example: Tier E (10-12 GB VRAM)\nollama pull qwen2.5:14b-instruct-q4_K_M   # MAIN\nollama pull qwen2.5:7b-instruct-q4_K_M    # FAST\nollama pull qwen2.5:3b                     # TINY"
    ),
    # Step 3 Tier G example
    (
        "# Example: Tier G (24 GB VRAM)\nollama pull qwen2.5:32b-instruct-q4_K_M   # MAIN\nollama pull qwen2.5:7b-instruct-q4_K_M    # FAST\nollama pull qwen2.5:3b                     # TINY",
        "# Example: Tier G (24 GB VRAM)\nollama pull qwen2.5:32b-instruct-q4_K_M   # MAIN\nollama pull qwen2.5:7b-instruct-q8_0      # FAST\nollama pull qwen2.5:3b                     # TINY"
    ),
    # Per-tier Tier A block
    (
        "### Tier A — CPU · 16 GB RAM\n```bash\nollama pull qwen2.5:7b-instruct-q4_K_M\nollama pull qwen2.5:1.5b\n\nclaude mcp add localthink \\\n  --env OLLAMA_MODEL=\"qwen2.5:7b-instruct-q4_K_M\" \\\n  --env OLLAMA_FAST_MODEL=\"qwen2.5:1.5b\" \\\n  --env OLLAMA_TINY_MODEL=\"qwen2.5:1.5b\" \\\n  -- uvx localthink-mcp\n```",
        "### Tier A — CPU · 16 GB RAM\n```bash\nollama pull qwen2.5:7b-instruct-q4_K_M\nollama pull qwen2.5:3b\nollama pull qwen2.5:1.5b\n\nclaude mcp add localthink \\\n  --env OLLAMA_MODEL=\"qwen2.5:7b-instruct-q4_K_M\" \\\n  --env OLLAMA_FAST_MODEL=\"qwen2.5:3b\" \\\n  --env OLLAMA_TINY_MODEL=\"qwen2.5:1.5b\" \\\n  -- uvx localthink-mcp\n```"
    ),
    # Per-tier Tier A+ block
    (
        "### Tier A+ — CPU · 32 GB RAM\n```bash\nollama pull qwen2.5:14b-instruct-q4_K_M\nollama pull qwen2.5:3b\n\nclaude mcp add localthink \\\n  --env OLLAMA_MODEL=\"qwen2.5:14b-instruct-q4_K_M\" \\\n  --env OLLAMA_FAST_MODEL=\"qwen2.5:3b\" \\\n  --env OLLAMA_TINY_MODEL=\"qwen2.5:3b\" \\\n  -- uvx localthink-mcp\n```",
        "### Tier A+ — CPU · 32 GB RAM\n```bash\nollama pull qwen2.5:14b-instruct-q4_K_M\nollama pull qwen2.5:7b-instruct-q4_K_M\nollama pull qwen2.5:3b\n\nclaude mcp add localthink \\\n  --env OLLAMA_MODEL=\"qwen2.5:14b-instruct-q4_K_M\" \\\n  --env OLLAMA_FAST_MODEL=\"qwen2.5:7b-instruct-q4_K_M\" \\\n  --env OLLAMA_TINY_MODEL=\"qwen2.5:3b\" \\\n  -- uvx localthink-mcp\n```"
    ),
    # Per-tier Tier B block
    (
        "### Tier B — 4 GB VRAM (GTX 1650, RX 580)\n```bash\nollama pull qwen2.5:7b-instruct-q4_K_M\nollama pull qwen2.5:1.5b\n\nclaude mcp add localthink \\\n  --env OLLAMA_MODEL=\"qwen2.5:7b-instruct-q4_K_M\" \\\n  --env OLLAMA_FAST_MODEL=\"qwen2.5:1.5b\" \\\n  --env OLLAMA_TINY_MODEL=\"qwen2.5:1.5b\" \\\n  -- uvx localthink-mcp\n```",
        "### Tier B — 4 GB VRAM (GTX 1650, RX 580)\n```bash\nollama pull qwen2.5:7b-instruct-q4_K_M\nollama pull qwen2.5:3b\nollama pull qwen2.5:1.5b\n\nclaude mcp add localthink \\\n  --env OLLAMA_MODEL=\"qwen2.5:7b-instruct-q4_K_M\" \\\n  --env OLLAMA_FAST_MODEL=\"qwen2.5:3b\" \\\n  --env OLLAMA_TINY_MODEL=\"qwen2.5:1.5b\" \\\n  -- uvx localthink-mcp\n```"
    ),
    # Per-tier Tier C block
    (
        "### Tier C — 6 GB VRAM (GTX 1660, RTX 2060)\n```bash\nollama pull qwen2.5:7b-instruct-q6_K\nollama pull qwen2.5:3b\n\nclaude mcp add localthink \\\n  --env OLLAMA_MODEL=\"qwen2.5:7b-instruct-q6_K\" \\\n  --env OLLAMA_FAST_MODEL=\"qwen2.5:3b\" \\\n  --env OLLAMA_TINY_MODEL=\"qwen2.5:3b\" \\\n  -- uvx localthink-mcp\n```",
        "### Tier C — 6 GB VRAM (GTX 1660, RTX 2060)\n```bash\nollama pull qwen2.5:7b-instruct-q6_K\nollama pull qwen2.5:3b\nollama pull qwen2.5:1.5b\n\nclaude mcp add localthink \\\n  --env OLLAMA_MODEL=\"qwen2.5:7b-instruct-q6_K\" \\\n  --env OLLAMA_FAST_MODEL=\"qwen2.5:3b\" \\\n  --env OLLAMA_TINY_MODEL=\"qwen2.5:1.5b\" \\\n  -- uvx localthink-mcp\n```"
    ),
    # Per-tier Tier D block
    (
        "### Tier D — 8 GB VRAM (RTX 3070, RX 6700 XT)\n```bash\nollama pull qwen2.5:7b-instruct-q8_0\nollama pull qwen2.5:3b\n\nclaude mcp add localthink \\\n  --env OLLAMA_MODEL=\"qwen2.5:7b-instruct-q8_0\" \\\n  --env OLLAMA_FAST_MODEL=\"qwen2.5:3b\" \\\n  --env OLLAMA_TINY_MODEL=\"qwen2.5:3b\" \\\n  -- uvx localthink-mcp\n```",
        "### Tier D — 8 GB VRAM (RTX 3070, RX 6700 XT)\n```bash\nollama pull qwen2.5:7b-instruct-q8_0\nollama pull qwen2.5:3b\nollama pull qwen2.5:1.5b\n\nclaude mcp add localthink \\\n  --env OLLAMA_MODEL=\"qwen2.5:7b-instruct-q8_0\" \\\n  --env OLLAMA_FAST_MODEL=\"qwen2.5:3b\" \\\n  --env OLLAMA_TINY_MODEL=\"qwen2.5:1.5b\" \\\n  -- uvx localthink-mcp\n```"
    ),
    # Per-tier Tier E block
    (
        "### Tier E — 10-12 GB VRAM (RTX 3080, RTX 4070)\n```bash\nollama pull qwen2.5:14b-instruct-q4_K_M\nollama pull qwen2.5:3b\n\nclaude mcp add localthink \\\n  --env OLLAMA_MODEL=\"qwen2.5:14b-instruct-q4_K_M\" \\\n  --env OLLAMA_FAST_MODEL=\"qwen2.5:3b\" \\\n  --env OLLAMA_TINY_MODEL=\"qwen2.5:3b\" \\\n  -- uvx localthink-mcp\n```\n*Optional upgrade: pull `qwen2.5:7b-instruct-q4_K_M` and set it as FAST in local_config for better classify/outline quality.*",
        "### Tier E — 10-12 GB VRAM (RTX 3080, RTX 4070)\n```bash\nollama pull qwen2.5:14b-instruct-q4_K_M\nollama pull qwen2.5:7b-instruct-q4_K_M\nollama pull qwen2.5:3b\n\nclaude mcp add localthink \\\n  --env OLLAMA_MODEL=\"qwen2.5:14b-instruct-q4_K_M\" \\\n  --env OLLAMA_FAST_MODEL=\"qwen2.5:7b-instruct-q4_K_M\" \\\n  --env OLLAMA_TINY_MODEL=\"qwen2.5:3b\" \\\n  -- uvx localthink-mcp\n```"
    ),
    # Per-tier Tier G block
    (
        "### Tier G — 24 GB VRAM (RTX 3090, RTX 4090)\n```bash\nollama pull qwen2.5:32b-instruct-q4_K_M\nollama pull qwen2.5:7b-instruct-q4_K_M\nollama pull qwen2.5:3b\n\nclaude mcp add localthink \\\n  --env OLLAMA_MODEL=\"qwen2.5:32b-instruct-q4_K_M\" \\\n  --env OLLAMA_FAST_MODEL=\"qwen2.5:7b-instruct-q4_K_M\" \\\n  --env OLLAMA_TINY_MODEL=\"qwen2.5:3b\" \\\n  -- uvx localthink-mcp\n```",
        "### Tier G — 24 GB VRAM (RTX 3090, RTX 4090)\n```bash\nollama pull qwen2.5:32b-instruct-q4_K_M\nollama pull qwen2.5:7b-instruct-q8_0\nollama pull qwen2.5:3b\n\nclaude mcp add localthink \\\n  --env OLLAMA_MODEL=\"qwen2.5:32b-instruct-q4_K_M\" \\\n  --env OLLAMA_FAST_MODEL=\"qwen2.5:7b-instruct-q8_0\" \\\n  --env OLLAMA_TINY_MODEL=\"qwen2.5:3b\" \\\n  -- uvx localthink-mcp\n```"
    ),
    # Apple M1/M2/M3 8GB
    (
        "# M1/M2/M3 — 8 GB\nollama pull qwen2.5:7b-instruct-q4_K_M && ollama pull qwen2.5:1.5b\nclaude mcp add localthink \\\n  --env OLLAMA_MODEL=\"qwen2.5:7b-instruct-q4_K_M\" \\\n  --env OLLAMA_FAST_MODEL=\"qwen2.5:1.5b\" \\\n  --env OLLAMA_TINY_MODEL=\"qwen2.5:1.5b\" \\\n  -- uvx localthink-mcp",
        "# M1/M2/M3 — 8 GB\nollama pull qwen2.5:7b-instruct-q4_K_M && ollama pull qwen2.5:3b && ollama pull qwen2.5:1.5b\nclaude mcp add localthink \\\n  --env OLLAMA_MODEL=\"qwen2.5:7b-instruct-q4_K_M\" \\\n  --env OLLAMA_FAST_MODEL=\"qwen2.5:3b\" \\\n  --env OLLAMA_TINY_MODEL=\"qwen2.5:1.5b\" \\\n  -- uvx localthink-mcp"
    ),
    # Apple M Pro 16-24GB
    (
        "# M Pro — 16-24 GB\nollama pull qwen2.5:14b-instruct-q4_K_M && ollama pull qwen2.5:3b\nclaude mcp add localthink \\\n  --env OLLAMA_MODEL=\"qwen2.5:14b-instruct-q4_K_M\" \\\n  --env OLLAMA_FAST_MODEL=\"qwen2.5:3b\" \\\n  --env OLLAMA_TINY_MODEL=\"qwen2.5:3b\" \\\n  -- uvx localthink-mcp",
        "# M Pro — 16-24 GB\nollama pull qwen2.5:14b-instruct-q4_K_M && ollama pull qwen2.5:7b-instruct-q4_K_M && ollama pull qwen2.5:3b\nclaude mcp add localthink \\\n  --env OLLAMA_MODEL=\"qwen2.5:14b-instruct-q4_K_M\" \\\n  --env OLLAMA_FAST_MODEL=\"qwen2.5:7b-instruct-q4_K_M\" \\\n  --env OLLAMA_TINY_MODEL=\"qwen2.5:3b\" \\\n  -- uvx localthink-mcp"
    ),
    # Apple M Max 32-40GB
    (
        "# M Max — 32-40 GB\nollama pull qwen2.5:32b-instruct-q4_K_M && ollama pull qwen2.5:7b-instruct-q4_K_M && ollama pull qwen2.5:3b\nclaude mcp add localthink \\\n  --env OLLAMA_MODEL=\"qwen2.5:32b-instruct-q4_K_M\" \\\n  --env OLLAMA_FAST_MODEL=\"qwen2.5:7b-instruct-q4_K_M\" \\\n  --env OLLAMA_TINY_MODEL=\"qwen2.5:3b\" \\\n  -- uvx localthink-mcp",
        "# M Max — 32-40 GB\nollama pull qwen2.5:32b-instruct-q4_K_M && ollama pull qwen2.5:7b-instruct-q8_0 && ollama pull qwen2.5:3b\nclaude mcp add localthink \\\n  --env OLLAMA_MODEL=\"qwen2.5:32b-instruct-q4_K_M\" \\\n  --env OLLAMA_FAST_MODEL=\"qwen2.5:7b-instruct-q8_0\" \\\n  --env OLLAMA_TINY_MODEL=\"qwen2.5:3b\" \\\n  -- uvx localthink-mcp"
    ),
]

ok = 0
missing = 0
for old, new in replacements:
    if old not in text:
        print(f"MISSING: {old[:70]!r}")
        missing += 1
    else:
        text = text.replace(old, new, 1)
        ok += 1

p.write_text(text, encoding="utf-8")
print(f"\n{ok} replacements applied, {missing} not found. Written to {p}")
