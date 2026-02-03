#!/usr/bin/env python

import argparse
import pathlib
import random
import sys

DEFAULT_FILES = ("wizard_names.txt", "wizard_elements.txt", "wizard_from.txt")


def random_wiz_property(wizprop):
    line = next(wizprop)
    for num, aline in enumerate(wizprop):
        if random.randrange(num + 2):
            continue
        line = aline
    return line


def load_random_line(path):
    try:
        with path.open("r", encoding="utf-8") as handle:
            return random_wiz_property(handle).strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"Missing data file: {path}")
    except StopIteration:
        raise ValueError(f"Data file is empty: {path}")


def build_wizard_description(files):
    wizard_property = [load_random_line(path) for path in files]
    return f"{wizard_property[0]} {wizard_property[1]} from {wizard_property[2]}"


def parse_args():
    parser = argparse.ArgumentParser(description="Generate random wizard descriptions.")
    parser.add_argument(
        "--count",
        type=int,
        default=1,
        help="Number of wizards to generate (default: 1).",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Seed for the random generator to get repeatable output.",
    )
    parser.add_argument(
        "--files",
        nargs=3,
        metavar=("NAMES", "ELEMENTS", "ORIGINS"),
        help="Custom data files to use instead of defaults.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    if args.count < 1:
        raise ValueError("--count must be at least 1")
    if args.seed is not None:
        random.seed(args.seed)
    files = args.files or DEFAULT_FILES
    file_paths = [pathlib.Path(file_name) for file_name in files]

    for _ in range(args.count):
        print(build_wizard_description(file_paths))


if __name__ == "__main__":
    try:
        main()
    except (FileNotFoundError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
