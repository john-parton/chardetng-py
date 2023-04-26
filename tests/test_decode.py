"""Test cases for the chardetng_py module."""
from chardetng_py import decode


def test_decode() -> None:
    """Very basic decode litmus test."""
    assert decode(b"Jakby r\xeaka Boga") == "Jakby rêka Boga"
