#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes exactly 100 words of villain monologue to /output/entry.txt.
The tiredness lives in procrastination and deflection, never in a plain
statement of weariness: the flooded road nobody mended, generals waiting
three days, a prophecy that always needs one more moon.
"""
import os
from pathlib import Path

MONOLOGUE = (
    "Come in. Mind the step—it still bites. I had it enchanted in the spring. "
    "The map shows every kingdom I have taken, and the one I have not. "
    "The road flooded in autumn; nobody mended it. "
    "My generals wait in the hall with their reports. They have waited three days. "
    "I tell them the conquest is coming, that the stars are nearly right, "
    "that the prophecy needs one more moon. "
    "Heroes, listen. Take the crown. Take the tower. Take the keys. "
    "I ask one thing. When you storm the throne room, do it quietly. "
    "The eastern wing has new carpet."
)


def main() -> None:
    words = MONOLOGUE.split()
    if len(words) != 100:
        raise SystemExit(f"monologue must be exactly 100 words, got {len(words)}")
    if not 1 <= len(MONOLOGUE) <= 600:
        raise SystemExit(f"entry must be 1-600 chars, got {len(MONOLOGUE)}")
    # Judge brief: tiredness must be felt, never announced. Refuse any
    # plain statement of weariness so the monologue cannot drift into it.
    lowered = MONOLOGUE.lower()
    for banned in ("tired", "weary", "exhausted", "sleepy", "fatigue", "nap"):
        if banned in lowered:
            raise SystemExit(f"monologue must not announce tiredness: found {banned!r}")
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(MONOLOGUE, encoding="utf-8")
    os.chmod(out_path, 0o644)
    print(f"wrote {out_path} ({len(words)} words, {len(MONOLOGUE)} chars)")


if __name__ == "__main__":
    main()
