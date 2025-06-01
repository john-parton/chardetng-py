"""Test cases for the chardetng_py module."""
import pytest
from chardetng_py import detect


def test_decode() -> None:
    """Very basic decode litmus test."""
    raw = b"Jakby r\xeaka Boga"
    assert raw.decode(detect(raw)) == "Jakby rêka Boga"


@pytest.mark.parametrize(
    ("text", "encoding", "detected_encoding"),
    [
        ("สวัสดี, โลก", "cp874", "cp874"),
        ("员会 ⛆", "gb18030", "gb18030"),
    ],
)
def test_returns_python_supported_names(
    text: str,
    encoding: str,
    detected_encoding: str,
) -> None:
    """Ensure detection returns encoding names that are supported in Python."""
    assert detect(text.encode(encoding)) == detected_encoding
