"""The Meeting That Should Have Been One Line.

Writes the single sentence that could have replaced an entire pointless
meeting to entry.txt in MAKEFUN_OUTPUT_DIR (default /output).
"""

import os
import stat

TEXT = (
    "I attended 47 minutes of a meeting I was invited to by mistake, "
    "took 1,847 lines of notes, and the only decision was to invite me "
    "again next week."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Gate: UTF-8, 1-200 chars, not only whitespace, one line, one sentence.
    assert 1 <= len(TEXT) <= 200, f"entry is {len(TEXT)} chars"
    assert TEXT.strip(), "entry is only whitespace"
    assert "\n" not in TEXT, "entry must be one line"
    assert TEXT.count(".") == 1, "entry must be a single sentence"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
