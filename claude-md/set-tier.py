#!/usr/bin/env python3
"""
Switch localthink instruction tier in ~/.claude/CLAUDE.md.

Replaces the managed localthink block with the chosen tier's content.
The block is bookmarked with HTML comments so it can be swapped safely
without touching the rest of CLAUDE.md.

Usage:
  python set-tier.py              # show current tier
  python set-tier.py full         # all 49 tools (~60 lines)
  python set-tier.py half         # file reads + execution filters (~35 lines)
  python set-tier.py quarter      # token-saving essentials only (~15 lines)

Copy the claude-md/ directory next to your CLAUDE.md, or update TIER_DIR below.
"""
import sys
import re
from pathlib import Path

CLAUDE_MD = Path.home() / ".claude" / "CLAUDE.md"
TIER_DIR  = Path(__file__).parent
VALID_TIERS = ("full", "half", "quarter")

_START = "<!-- localthink-tier-start -->"
_END   = "<!-- localthink-tier-end -->"
_TIER_RE = re.compile(r"<!-- localthink-tier: (\w+) -->")


def _read_tier(tier: str) -> str:
    path = TIER_DIR / f"tier-{tier}.md"
    if not path.exists():
        sys.exit(f"Tier file not found: {path}\n"
                 f"Make sure tier-{tier}.md is in the same directory as set-tier.py")
    return path.read_text(encoding="utf-8").strip()


def get_current_tier(text: str) -> str:
    m = _TIER_RE.search(text)
    return m.group(1) if m else "unknown"


def set_tier(tier: str) -> None:
    if not CLAUDE_MD.exists():
        sys.exit(f"CLAUDE.md not found: {CLAUDE_MD}")

    text = CLAUDE_MD.read_text(encoding="utf-8")
    tier_content = _read_tier(tier)
    current = get_current_tier(text)

    new_block = (
        f"{_START}\n"
        f"<!-- localthink-tier: {tier} -->\n"
        f"{tier_content}\n"
        f"{_END}"
    )

    if _START in text and _END in text:
        # Swap the existing managed block
        new_text = re.sub(
            re.escape(_START) + r".*?" + re.escape(_END),
            new_block,
            text,
            flags=re.DOTALL,
        )
    else:
        # No managed block yet — strip any unmanaged localthink section and append.
        # Pattern handles both "## Localthink" at start-of-file and after a newline.
        new_text = re.sub(
            r"(^|\n)## Localthink\b.*?(?=\n## |\Z)",
            "",
            text,
            flags=re.DOTALL,
        ).strip() + f"\n\n{new_block}\n"

    CLAUDE_MD.write_text(new_text, encoding="utf-8")
    line_count = len(tier_content.splitlines())
    print(f"Switched: {current} -> {tier}  ({line_count} lines injected into CLAUDE.md)")


def show_status() -> None:
    if not CLAUDE_MD.exists():
        print(f"CLAUDE.md not found: {CLAUDE_MD}")
        return
    text = CLAUDE_MD.read_text(encoding="utf-8")
    tier = get_current_tier(text)

    lines_in_block = 0
    if _START in text and _END in text:
        block = text[text.index(_START):text.index(_END) + len(_END)]
        lines_in_block = block.count("\n")

    print(f"Current tier : {tier}")
    print(f"Block size   : {lines_in_block} lines in CLAUDE.md")
    print(f"CLAUDE.md    : {CLAUDE_MD}")
    print(f"Tier files   : {TIER_DIR}")
    print()
    print(f"Usage: python set-tier.py [{' | '.join(VALID_TIERS)}]")
    print()
    print("  full    — all 49 tools (~60 lines)")
    print("  half    — file reads + execution filters (~35 lines)")
    print("  quarter — token-saving essentials only (~15 lines)")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_status()
        sys.exit(0)

    tier = sys.argv[1].lower()
    if tier not in VALID_TIERS:
        print(f"Invalid tier '{tier}'. Choose: {' | '.join(VALID_TIERS)}")
        sys.exit(1)

    set_tier(tier)
