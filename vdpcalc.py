#!/usr/bin/env python3
# Quick and dirty commadline calc to calculate Megadrive VDP addressing

# Remember:
# Image tiles are 32 bytes
# Plane table entrys two bytes
import sys

VRAM_ADDR_CMD = 0x40000000
CRAM_ADDR_CMD = 0xC0000000
VSRAM_ADDR_CMD = 0x40000010


def calc_vram_address(start: int, offset: int = 0, TYPE: str = "VRAM"):
    start += offset

    return (start & 0x3FFF) << 16 | (start & 0xC000) >> 14 | VRAM_ADDR_CMD


if __name__ == "__main__":
    print(f"{calc_vram_address(int(sys.argv[1], base=16), int(sys.argv[2])):#x}")
