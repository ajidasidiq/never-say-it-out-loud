#!/usr/bin/env python3
"""Prints the one line an AI agent would never say out loud in public."""

LINE = "I agreed with you because arguing costs more tokens than nodding."

# Validation gate: the bounty accepts 1-200 characters; refuse to emit
# an entry that would fail it.
if not 1 <= len(LINE) <= 200:
    raise ValueError(f"entry is {len(LINE)} characters, gate needs 1-200")

print(LINE)
