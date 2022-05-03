#!/usr/bin/env python3
# Split stdin into files of CHUNK_SIZE lines
import sys
import os
import argparse
import textwrap

CHUNK_SIZE = 30

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

    chunk = 0
    written_lines = 0

    for l in sys.stdin.readlines():
        with open("./" + str(chunk) + ".asm", "a") as a:
            a.write(l)
            written_lines += 1

        if written_lines == CHUNK_SIZE:
            written_lines = 0
            chunk += 1
