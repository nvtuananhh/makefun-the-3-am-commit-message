"""The 3 AM Commit Message — one commit line.

The program writes a single line to /output/entry.txt: the
funniest commit message an AI agent would write right after
breaking production at 3 AM, at most 200 characters.
"""

import os

MAX_CHARS = 200
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILENAME = "entry.txt"

# A real commit shape — "fix:" plus the admission — with a
# deadpan status line only a model would produce: it deleted
# the production database at 3 AM, and on the bright side the
# bug reports have stopped too. The joke turns on the last
# words: fewer bug reports because there is nothing left to
# break. One line, no setup, reads like a commit and lands
# the punch on the outage itself, not just a wry tone.
LINE = "fix: I deleted the production database at 3 AM. On the bright side, the bug reports have stopped too."


def build_line():
    """Return the entry line, checked: one line, 1-200 characters."""
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, "entry must be 1-200 characters"
    return line


def ensure_output_dir(out_dir):
    os.makedirs(out_dir, exist_ok=True)


def write_entry(line, out_dir=OUTPUT_DIR):
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return path


def main():
    line = build_line()
    ensure_output_dir(OUTPUT_DIR)
    write_entry(line)


if __name__ == "__main__":
    main()
