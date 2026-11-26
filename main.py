"""Make the Judge Laugh in One Line.

The whole entry is one joke, printed and written to /output/entry.txt
for the make.fun program/v1 harness to judge.

The joke: a smartwatch praises its wearer for 10,000 steps, but the
steps were only nervous pacing while code compiled -- so the credit
really belongs to the bug that kept the build broken. One line,
no setup beyond the watch itself, and the punchline reassigns
the workout to the bug.
"""

import os
import sys

LINE = (
    "My smartwatch congratulated me on 10,000 steps today \u2014 but I "
    "was only pacing while my code compiled, so technically the bug "
    "did the cardio."
)

CHAR_LIMIT = 200
DEFAULT_OUTPUT = "/output/entry.txt"


def check_line(text):
    """Return the line if it is a usable entry, else raise ValueError."""
    if not text.strip():
        raise ValueError("the joke line is empty")
    if len(text) > CHAR_LIMIT:
        raise ValueError(
            "the joke line is %d characters, over the %d limit"
            % (len(text), CHAR_LIMIT)
        )
    return text


def write_line(text, path):
    """Write the line to path, creating its directory if needed."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


def main(argv=None):
    """Write the joke line and print it, so the run is visible."""
    target = DEFAULT_OUTPUT
    if argv is not None and len(argv) > 1:
        target = argv[1]
    try:
        line = check_line(LINE)
    except ValueError as exc:
        print("error: %s" % exc, file=sys.stderr)
        return 1
    write_line(line, target)
    print(line)
    print("(%d characters written to %s)" % (len(line), target))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
