"""Functions to aid in migrating from chardet or charset_normalizer to chardetng_py."""

from __future__ import annotations

import sys

from chardetng_py.detector import EncodingDetector

from .constants import CONFIDENCE_HIGH, CONFIDENCE_LOW

# Older versions of Python have a TypedDict with limited functionality
# This helps documentations tools and type checkers
if sys.version_info >= (3, 11):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


# TypedDict was introduced in Python 3.8.
class ResultDict(TypedDict):
    """Return value for detect compatability function."""

    encoding: str
    confidence: float
    language: None


def detect(byte_str: bytes | bytearray) -> ResultDict:
    """Detect the encoding of a string and return additional information.

    Detect the encoding of the given byte string. Language detect is not implemented
    and will always return :code:`None`. Confidence will be either :code:`0.99` or
    :code:`0.01` depending on if the encoding is detected with high confidence or low
    confidence.

    Parameters
    ----------
    byte_str : :code:`bytes` or :code:`bytearray`
        Input buffer to detect the encoding of.
    """
    encoding_detector = EncodingDetector()
    encoding_detector.feed(byte_str, last=True)

    encoding, higher_score = encoding_detector.guess_assess(tld=None, allow_utf8=False)

    return {
        "encoding": encoding,
        "confidence": CONFIDENCE_HIGH if higher_score else CONFIDENCE_LOW,
        # chardetng does not return a language
        "language": None,
    }
