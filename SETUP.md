# Localthink MCP — Setup Guide

Everything runs through CLI or the built-in `local_config` GUI. No config file editing required.

---

## Quick install (5 commands)

```bash
# 1. Pull models for your hardware (see tier table below — Tier E shown)
ollama pull qwen2.5:14b-instruct-q4_K_M
ollama pull qwen2.5:3b

# 2. Register with Claude Code — models set inline, nothing to edit
claude mcp add localthink \
  --env OLLAMA_MODEL="qwen2.5:14b-instruct-q4_K_M" \
  --env OLLAMA_FAST_MODEL="qwen2.5:3b" \
  --env OLLAMA_TINY_MODEL="qwen2.5:3b" \
  -- uvx localthink-mcp

# 3. Set your CLAUDE.md instruction tier
cp -r claude-md/ ~/.claude/localthink/
python ~/.claude/localthink/set-tier.py full

# 4. Verify
claude mcp list   # localthink → Connected
```

**Windows:**
```bash
claude mcp add --transport stdio localthink ^
  --env OLLAMA_MODEL="qwen2.5:14b-instruct-q4_K_M" ^
  --env OLLAMA_FAST_MODEL="qwen2.5:3b" ^
  --env OLLAMA_TINY_MODEL="qwen2.5:3b" ^
  -- cmd /c uvx localthink-mcp

xcopy claude-md\* %USERPROFILE%\.claude\localthink\ /E /I /Y
python %USERPROFILE%\.claude\localthink\set-tier.py full
```

Substitute models for your hardware using the tier table below. Fine-tune everything else with `local_config` — no file editing needed.

---

## Hardware tier table

| Tier | Hardware | MAIN model | FAST model | TINY model | Speed (tok/s) |
|------|----------|-----------|------------|------------|---------------|
| A | CPU · 16 GB RAM | `qwen2.5:7b-instruct-q4_K_M` | `qwen2.5:1.5b` | `qwen2.5:1.5b` | 3-8 |
| A+ | CPU · 32 GB RAM | `qwen2.5:14b-instruct-q4_K_M` | `qwen2.5:3b` | `qwen2.5:3b` | 2-5 |
| B | 4 GB VRAM | `qwen2.5:7b-instruct-q4_K_M` | `qwen2.5:1.5b` | `qwen2.5:1.5b` | 20-40 |
| C | 6 GB VRAM | `qwen2.5:7b-instruct-q6_K` | `qwen2.5:3b` | `qwen2.5:3b` | 25-45 |
| D | 8 GB VRAM | `qwen2.5:7b-instruct-q8_0` | `qwen2.5:3b` | `qwen2.5:3b` | 30-55 |
| E | 10-12 GB VRAM | `qwen2.5:14b-instruct-q4_K_M` | `qwen2.5:3b` | `qwen2.5:3b` | 20-40 |
| F | 16-20 GB VRAM | `qwen2.5:14b-instruct-q8_0` | `qwen2.5:7b-instruct-q4_K_M` | `qwen2.5:3b` | 20-35 |
| G | 24 GB VRAM | `qwen2.5:32b-instruct-q4_K_M` | `qwen2.5:7b-instruct-q4_K_M` | `qwen2.5:3b` | 15-30 |
| H | 48 GB+ VRAM | `qwen2.5:72b-instruct-q4_K_M` | `qwen2.5:14b-instruct-q4_K_M` | `qwen2.5:3b` | 8-18 |
| Apple M · 8 GB | M1/M2/M3 base | `qwen2.5:7b-instruct-q4_K_M` | `qwen2.5:1.5b` | `qwen2.5:1.5b` | 15-30 |
| Apple M · 16-24 GB | M Pro | `qwen2.5:14b-instruct-q4_K_M` | `qwen2.5:3b` | `qwen2.5:3b` | 20-45 |
| Apple M · 32-40 GB | M Max | `qwen2.5:32b-instruct-q4_K_M` | `qwen2.5:7b-instruct-q4_K_M` | `qwen2.5:3b` | 15-30 |
| Apple M · 64+ GB | M Ultra | `qwen2.5:72b-instruct-q4_K_M` | `qwen2.5:14b-instruct-q4_K_M` | `qwen2.5:3b` | 10-25 |

> **Three model tiers explained:**
> - **MAIN** — all deep operations: summarize, answer, find_impl, pipeline, audit
> - **FAST** — lightweight ops: classify, outline, symbols, code_surface, translate, schema_infer
> - **TINY** — instant yes/no: gate, route decisions, hallucination check

---

## Step-by-step

### 1. Install Ollama

**Windows / macOS:** Download and run the installer from [ollama.ai](https://ollama.ai).

**Linux:**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

Verify:
```bash
ollama serve
curl http://localhost:11434/api/tags   # {"models":[...]}
```

### 2. GPU prerequisites

| GPU | What you need |
|-----|--------------|
| NVIDIA | CUDA 11.8+ driver — `nvidia-smi` to verify |
| AMD (Linux) | ROCm 5.7+ — `sudo apt install rocm-hip-sdk` |
| AMD (Windows) | DirectML — automatic, nothing to install |
| Apple Silicon | Metal — automatic |
| CPU only | Nothing extra |

### 3. Pull models for your tier

Find your tier in the table above and run one `ollama pull` per model:

```bash
# Example: Tier E (10-12 GB VRAM)
ollama pull qwen2.5:14b-instruct-q4_K_M   # MAIN
ollama pull qwen2.5:3b                     # FAST + TINY
```

```bash
# Example: Tier G (24 GB VRAM)
ollama pull qwen2.5:32b-instruct-q4_K_M   # MAIN
ollama pull qwen2.5:7b-instruct-q4_K_M    # FAST
ollama pull qwen2.5:3b                     # TINY
```

### 4. Register with Claude Code

Pass your three model names directly on the command line. No JSON editing.

```bash
# macOS / Linux
claude mcp add localthink \
  --env OLLAMA_MODEL="<MAIN model>" \
  --env OLLAMA_FAST_MODEL="<FAST model>" \
  --env OLLAMA_TINY_MODEL="<TINY model>" \
  -- uvx localthink-mcp
```

```bash
# Windows
claude mcp add --transport stdio localthink ^
  --env OLLAMA_MODEL="<MAIN model>" ^
  --env OLLAMA_FAST_MODEL="<FAST model>" ^
  --env OLLAMA_TINY_MODEL="<TINY model>" ^
  -- cmd /c uvx localthink-mcp
```

**Changing models later?** Use the `local_config` GUI — no need to re-register.

### 5. Set your CLAUDE.md instruction tier

Copy the tier files to your Claude config folder, then pick a tier:

```bash
# macOS / Linux
cp -r claude-md/ ~/.claude/localthink/
python ~/.claude/localthink/set-tier.py full
```

```bash
# Windows
xcopy claude-md\* %USERPROFILE%\.claude\localthink\ /E /I /Y
python %USERPROFILE%\.claude\localthink\set-tier.py full
```

| Tier | Lines injected | Tools available | Best for |
|------|----------------|-----------------|----------|
| `full` | ~55 | All 45 | Complex projects, new codebases |
| `half` | ~30 | ~18 | Daily dev: file nav + CI filters |
| `quarter` | ~12 | ~6 | Minimal — just stop big-file loads |

Switch at any time:
```bash
python ~/.claude/localthink/set-tier.py half
python ~/.claude/localthink/set-tier.py        # show current
```

### 6. Verify

```bash
claude mcp list        # localthink → Connected
# Then in Claude Code:
# local_models()       # shows MAIN / FAST / TINY tiers + Ollama health
```

---

## Per-tier install commands

### Tier A — CPU · 16 GB RAM
```bash
ollama pull qwen2.5:7b-instruct-q4_K_M
ollama pull qwen2.5:1.5b

claude mcp add localthink \
  --env OLLAMA_MODEL="qwen2.5:7b-instruct-q4_K_M" \
  --env OLLAMA_FAST_MODEL="qwen2.5:1.5b" \
  --env OLLAMA_TINY_MODEL="qwen2.5:1.5b" \
  -- uvx localthink-mcp
```
*Tip: Set `LOCALTHINK_MAX_CONCURRENCY=1` in local_config → Limits if RAM is tight.*

### Tier A+ — CPU · 32 GB RAM
```bash
ollama pull qwen2.5:14b-instruct-q4_K_M
ollama pull qwen2.5:3b

claude mcp add localthink \
  --env OLLAMA_MODEL="qwen2.5:14b-instruct-q4_K_M" \
  --env OLLAMA_FAST_MODEL="qwen2.5:3b" \
  --env OLLAMA_TINY_MODEL="qwen2.5:3b" \
  -- uvx localthink-mcp
```

### Tier B — 4 GB VRAM (GTX 1650, RX 580)
```bash
ollama pull qwen2.5:7b-instruct-q4_K_M
ollama pull qwen2.5:1.5b

claude mcp add localthink \
  --env OLLAMA_MODEL="qwen2.5:7b-instruct-q4_K_M" \
  --env OLLAMA_FAST_MODEL="qwen2.5:1.5b" \
  --env OLLAMA_TINY_MODEL="qwen2.5:1.5b" \
  -- uvx localthink-mcp
```
*The 7B Q4 needs ~4.7 GB peak — Ollama offloads a few layers to RAM if tight, which is fine with 16 GB+ system RAM.*

### Tier C — 6 GB VRAM (GTX 1660, RTX 2060)
```bash
ollama pull qwen2.5:7b-instruct-q6_K
ollama pull qwen2.5:3b

claude mcp add localthink \
  --env OLLAMA_MODEL="qwen2.5:7b-instruct-q6_K" \
  --env OLLAMA_FAST_MODEL="qwen2.5:3b" \
  --env OLLAMA_TINY_MODEL="qwen2.5:3b" \
  -- uvx localthink-mcp
```

### Tier D — 8 GB VRAM (RTX 3070, RX 6700 XT)
```bash
ollama pull qwen2.5:7b-instruct-q8_0
ollama pull qwen2.5:3b

claude mcp add localthink \
  --env OLLAMA_MODEL="qwen2.5:7b-instruct-q8_0" \
  --env OLLAMA_FAST_MODEL="qwen2.5:3b" \
  --env OLLAMA_TINY_MODEL="qwen2.5:3b" \
  -- uvx localthink-mcp
```
*Q8_0 is near-lossless quality at 7B — the sweet spot for this VRAM tier.*

### Tier E — 10-12 GB VRAM (RTX 3080, RTX 4070)
```bash
ollama pull qwen2.5:14b-instruct-q4_K_M
ollama pull qwen2.5:3b

claude mcp add localthink \
  --env OLLAMA_MODEL="qwen2.5:14b-instruct-q4_K_M" \
  --env OLLAMA_FAST_MODEL="qwen2.5:3b" \
  --env OLLAMA_TINY_MODEL="qwen2.5:3b" \
  -- uvx localthink-mcp
```
*Optional upgrade: pull `qwen2.5:7b-instruct-q4_K_M` and set it as FAST in local_config for better classify/outline quality.*

### Tier F — 16-20 GB VRAM (RTX 4080, A5000)
```bash
ollama pull qwen2.5:14b-instruct-q8_0
ollama pull qwen2.5:7b-instruct-q4_K_M
ollama pull qwen2.5:3b

claude mcp add localthink \
  --env OLLAMA_MODEL="qwen2.5:14b-instruct-q8_0" \
  --env OLLAMA_FAST_MODEL="qwen2.5:7b-instruct-q4_K_M" \
  --env OLLAMA_TINY_MODEL="qwen2.5:3b" \
  -- uvx localthink-mcp
```

### Tier G — 24 GB VRAM (RTX 3090, RTX 4090)
```bash
ollama pull qwen2.5:32b-instruct-q4_K_M
ollama pull qwen2.5:7b-instruct-q4_K_M
ollama pull qwen2.5:3b

claude mcp add localthink \
  --env OLLAMA_MODEL="qwen2.5:32b-instruct-q4_K_M" \
  --env OLLAMA_FAST_MODEL="qwen2.5:7b-instruct-q4_K_M" \
  --env OLLAMA_TINY_MODEL="qwen2.5:3b" \
  -- uvx localthink-mcp
```

### Tier H — 48 GB+ VRAM (A100, H100, dual 4090)
```bash
ollama pull qwen2.5:72b-instruct-q4_K_M
ollama pull qwen2.5:14b-instruct-q4_K_M
ollama pull qwen2.5:3b

claude mcp add localthink \
  --env OLLAMA_MODEL="qwen2.5:72b-instruct-q4_K_M" \
  --env OLLAMA_FAST_MODEL="qwen2.5:14b-instruct-q4_K_M" \
  --env OLLAMA_TINY_MODEL="qwen2.5:3b" \
  -- uvx localthink-mcp
```
*Multi-GPU: Ollama distributes layers automatically — no extra config.*

### Apple Silicon

```bash
# M1/M2/M3 — 8 GB
ollama pull qwen2.5:7b-instruct-q4_K_M && ollama pull qwen2.5:1.5b
claude mcp add localthink \
  --env OLLAMA_MODEL="qwen2.5:7b-instruct-q4_K_M" \
  --env OLLAMA_FAST_MODEL="qwen2.5:1.5b" \
  --env OLLAMA_TINY_MODEL="qwen2.5:1.5b" \
  -- uvx localthink-mcp

# M Pro — 16-24 GB
ollama pull qwen2.5:14b-instruct-q4_K_M && ollama pull qwen2.5:3b
claude mcp add localthink \
  --env OLLAMA_MODEL="qwen2.5:14b-instruct-q4_K_M" \
  --env OLLAMA_FAST_MODEL="qwen2.5:3b" \
  --env OLLAMA_TINY_MODEL="qwen2.5:3b" \
  -- uvx localthink-mcp

# M Max — 32-40 GB
ollama pull qwen2.5:32b-instruct-q4_K_M && ollama pull qwen2.5:7b-instruct-q4_K_M && ollama pull qwen2.5:3b
claude mcp add localthink \
  --env OLLAMA_MODEL="qwen2.5:32b-instruct-q4_K_M" \
  --env OLLAMA_FAST_MODEL="qwen2.5:7b-instruct-q4_K_M" \
  --env OLLAMA_TINY_MODEL="qwen2.5:3b" \
  -- uvx localthink-mcp

# M Ultra — 64-192 GB
ollama pull qwen2.5:72b-instruct-q4_K_M && ollama pull qwen2.5:14b-instruct-q4_K_M && ollama pull qwen2.5:3b
claude mcp add localthink \
  --env OLLAMA_MODEL="qwen2.5:72b-instruct-q4_K_M" \
  --env OLLAMA_FAST_MODEL="qwen2.5:14b-instruct-q4_K_M" \
  --env OLLAMA_TINY_MODEL="qwen2.5:3b" \
  -- uvx localthink-mcp
```

---

## Configuring after install — local_config GUI

All 18 settings are available in the GUI. Type this in Claude Code:

```
local_config
```

A desktop window opens immediately — no terminal, no file editing.

| Tab | What you configure |
|-----|--------------------|
| **Ollama** | Base URL · MAIN model · FAST model · TINY model |
| **Timeouts** | Per-tier response timeouts · health check · code_surface timeout |
| **Limits** | Max file bytes · pipeline steps · scan files · classify sample · concurrency |
| **Cache** | Cache directory · TTL (days) |
| **Memo** | Scratchpad directory · auto-compact threshold |

**Key settings to tune for your hardware:**

| Setting | Where | Low VRAM | High VRAM |
|---------|--------|----------|-----------|
| `LOCALTHINK_TIMEOUT` | Timeouts tab | `120` (7b fast) | `600` (32b+) |
| `LOCALTHINK_MAX_CONCURRENCY` | Limits tab | `1–2` | `6–8` |
| `LOCALTHINK_CACHE_TTL_DAYS` | Cache tab | `7` (tight disk) | `90` |

**Save** writes `~/.localthink-mcp/config.json` and hot-reloads instantly. Timeout, limit, cache, and memo changes apply immediately. Model and URL changes require reconnecting the server (`/mcp` → reconnect in Claude Code).

---

## Quantization reference

| Quant | VRAM vs FP16 | Quality | Use when |
|-------|-------------|---------|----------|
| `q3_K_M` | ~35% | Moderate | Need bigger model in tight VRAM |
| `q4_K_M` | ~50% | Low loss | **Default — best balance** |
| `q5_K_M` | ~60% | Very low | Extra headroom when VRAM permits |
| `q6_K` | ~75% | Minimal | When VRAM comfortably fits |
| `q8_0` | ~80% | Negligible | Near-lossless; use when fits easily |

Don't go below `q4_K_M` for the MAIN model — quality degrades for complex summarisation.

---

## Troubleshooting

**`[localthink] Ollama is not running`**
```bash
ollama serve
# Windows/macOS: check system tray icon
```

**Slow inference on GPU**
```bash
nvidia-smi   # GPU utilization should be 80-100% during inference
# If low: install/update CUDA drivers
```

**Out of memory**
```bash
# Switch to smaller quantization
ollama pull qwen2.5:7b-instruct-q4_K_M
# Then update model in local_config GUI (Ollama tab → Save)
```

**Change models without re-registering**
```
# In Claude Code:
local_config   # Ollama tab → update model fields → Save → reconnect MCP
```

**AMD on Windows not detected**
Ollama uses DirectML automatically on Windows 10 2004+ / Windows 11. Ensure drivers are current.

**`local_code_surface` wrong output on Python**
Pure AST extraction — no Ollama involved. If wrong, check for a syntax error:
```bash
python -m py_compile your_file.py
```
