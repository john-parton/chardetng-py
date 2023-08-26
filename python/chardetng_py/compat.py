"""Functions to aid in migrating from chardet or charset_normalizer to chardetng_py."""

import sys
from typing import Final, Union

from chardetng_py.shortcuts import detect as _detect

# Older versions of Python have a TypedDict with limited functionality
# This helps documentations tools and type checkers
if sys.version_info >= (3, 11):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


# chardetng does not return a confidence value
# This is the value which is unconditionally returned
DEFAULT_CONFIDENCE: Final[float] = 0.99


# TypedDict was introduced in Python 3.8.
class ResultDict(TypedDict):
    """Return value for detect compatability function."""

    encoding: str
    confidence: float
    language: None


def detect(byte_str: Union[bytes, bytearray]) -> ResultDict:
    """Detect the encoding of a string and return additional information.

    Detect the encoding of the given byte string. Language detect is not implemented
    and will always return :code:`None`. Confidence is always :code:`0.99`.

    Parameters
    ----------
    byte_str : :code:`bytes` or :code:`bytearray`
        Input buffer to detect the encoding of.
    """
    return {
        "encoding": _detect(byte_str),
        "confidence": DEFAULT_CONFIDENCE,
        # chardetng does not return a language
        "language": None,
    }
