"""Test for cert_test using badssl.com"""
import pytest
from cert_test import Cert

def test_is_valid():
    assert Cert("wrong.host.badssl.com").is_valid == False
    assert Cert("badssl.com").is_valid == True

def test_remaining_days():
    assert Cert("badssl.com").remaining_days > 1
