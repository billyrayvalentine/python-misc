import pytest
import vdpcalc


def test_vram_zero_start_zero_offset():
    assert vdpcalc.calc_vram_address(0, 0) == 0x40000000


def test_vram_zero_start_two_offset():
    assert vdpcalc.calc_vram_address(0, 2) == 0x40020000


def test_vram_zero_start_3072_offset():
    assert vdpcalc.calc_vram_address(0x0000, 3072) == 0x4C000000


def test_vram_0xE000_start_zero_offset():
    assert vdpcalc.calc_vram_address(0xE000, 0) == 0x60000003


def test_vram_0xA800_start_zero_offset():
    assert vdpcalc.calc_vram_address(0xA800, 0) == 0x68000002


def test_vram_0xC000_start_21504_offset():
    assert vdpcalc.calc_vram_address(0xC000, 1344) == 0x45400003
