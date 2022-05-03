#!/usr/bin/env python3
# Wrap stdin to 32 chars but preserve line break for paragraphs
import sys
import configparser
import os
import argparse
import textwrap


def process_line(line):
    """Wrap text but preserve blank lines as paragraph breaks"""
    if line == "\n":
        return "\n\n"
    else:
        return textwrap.fill(line, width=32, fix_sentence_endings=True)


if __name__ == "__main__":

    # Setup command line args
    parser = argparse.ArgumentParser(description="texttoslide")
    parser.add_argument(
        "-d",
        "--debug",
        choices=["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"],
        help="debug level",
        default="INFO",
    )

    args = parser.parse_args()

    processed_lines = map(process_line, sys.stdin.readlines())

    for l in processed_lines:
        sys.stdout.writelines(l)
