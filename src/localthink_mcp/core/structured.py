"""JSON-enforced generation using Ollama's format=json mode.

generate_structured() calls Ollama with format="json" so the output is
always syntactically valid JSON. One retry with a stricter nudge on parse
failure. Falls back to returning the raw string on second failure.
"""
from __future__ import annotations

import json


def generate_structured(prompt: str, system: str, model: str = "") -> dict | list:
    """Call Ollama in JSON mode; parse and return as dict/list. One retry on failure."""
    from ollama_client import generate_json  # imported here to respect sys.path setup

    raw = generate_json(prompt=prompt, system=system, model=model)
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        retry_prompt = f"{prompt}\n\nReturn valid JSON only — no markdown fences, no explanation."
        raw2 = generate_json(prompt=retry_prompt, system=system, model=model)
        try:
            return json.loads(raw2)
        except json.JSONDecodeError:
            return {"error": "json_parse_failed", "raw": raw2[:500]}


def render_as_text(data: dict | list | str) -> str:
    """Convert structured output to a plain text string for MCP tool output."""
    if isinstance(data, str):
        return data
    if isinstance(data, dict) and "error" in data:
        return data.get("raw", json.dumps(data, indent=2, ensure_ascii=False))
    return json.dumps(data, indent=2, ensure_ascii=False)
