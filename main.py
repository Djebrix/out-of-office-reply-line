"""Out-of-office auto-reply entry for make.fun.

Writes one funny one-line out-of-office reply to /output/entry.txt.
Deterministic: the same constant line, every run. Stdlib only.
"""

import os

SETUP = "Out of office until Monday. I left my to-do list in charge"
PUNCHLINE = "it has already resigned."

LINE = f"{SETUP} \u2014 {PUNCHLINE}"


def build_line() -> str:
    """Assemble the one-line reply from its setup and punchline."""
    return f"{SETUP} \u2014 {PUNCHLINE}"


MIN_CHARS = 1
MAX_CHARS = 160


def validate_line(line: str) -> None:
    """Enforce the competition's char gate before writing anything."""
    if not (MIN_CHARS <= len(line) <= MAX_CHARS):
        raise ValueError(
            f"entry line is {len(line)} chars, must be {MIN_CHARS}-{MAX_CHARS}"
        )


def main() -> None:
    line = build_line()
    validate_line(line)
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
