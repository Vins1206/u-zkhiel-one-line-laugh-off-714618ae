#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Writes exactly one funny line to /output/entry.txt.
Pure stdlib, deterministic: the same line on every run,
no randomness, no network, no environment input.
"""

import os

JOKE = "We held a funeral for my goldfish; the cat RSVP'd yes and brought a fork."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate the entry before writing: the sealed scorer requires UTF-8 text
    # of 1-200 characters, not only whitespace, on a single line. Shorter
    # also wins the size tie-break, so the line stays trimmed to the bone.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert "\n" not in JOKE, "joke must be a single line"
    assert JOKE.strip() == JOKE and JOKE.strip(), "joke must not be blank"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    print(f"Wrote {len(JOKE)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
