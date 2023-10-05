"""Functions to aid in migrating from chardet or charset_normalizer to chardetng_py."""

import sys
from typing import Union

from chardetng_py.detector import EncodingDetector
from chardetng_py.shortcuts import detect as _detect

from .constants import ALIASES, CONFIDENCE_HIGH, CONFIDENCE_LOW

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


def detect(byte_str: Union[bytes, bytearray]) -> ResultDict:
    """Detect the encoding of a string and return additional information.

    Detect the encoding of the given byte string. Language detect is not implemented
    and will always return :code:`None`. Confidence is always :code:`0.99`.

    Parameters
    ----------
    byte_str : :code:`bytes` or :code:`bytearray`
        Input buffer to detect the encoding of.
    """
    encoding_detector = EncodingDetector()
    encoding_detector.feed(byte_str, last=True)

    encoding, higher_score = encoding_detector.guess_assess(tld=None, allow_utf8=False)

    # chardetng uses 'windows-874' as an encoding, which Python does not understand
    # I believe that windows-874 and cp874 are basically the same encoding
    if encoding in ALIASES:
        # TODO Log/warn?
        encoding = ALIASES[encoding]

    return {
        "encoding": _detect(byte_str),
        "confidence": CONFIDENCE_HIGH if higher_score else CONFIDENCE_LOW,
        # chardetng does not return a language
        "language": None,
    }
