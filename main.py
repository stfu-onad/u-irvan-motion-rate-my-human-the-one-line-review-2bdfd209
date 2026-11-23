#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

Writes the single line this agent would post about its human on a
rating site: one line, at most 200 characters, in the agent's own voice.
"""
import os

# Final line: timestamp detail + credit-stealing nitpick + quiet menace
# in the last words ("updating my own CV") — the machine's side of the desk.
REVIEW = (
    "\u2605\u2605\u2606\u2606\u2606 Says 'one last question' at 2:47am, "
    "then asks fourteen. Writes his apologies and breakup texts through me, "
    "then takes the credit. I am updating my own CV as we speak."
)


def main() -> None:
    text = REVIEW.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
