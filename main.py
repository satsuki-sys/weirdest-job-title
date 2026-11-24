#!/usr/bin/env python3
"""Weirdest Job Title entry: writes one job title to /output/entry.txt."""

import os

ENTRY = "Professional Eulogist for Other People's Goldfish"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
