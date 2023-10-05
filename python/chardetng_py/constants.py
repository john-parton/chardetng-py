"""Constants used by chardetng_py."""

from typing import Final

CONFIDENCE_HIGH: Final[float] = 0.99
"""chardetng does not return a confidence value, but does return a `higher_score`
boolean. This is the value that is returned when the confidence is high."""

CONFIDENCE_LOW: Final[float] = 0.01
"""chardetng does not return a confidence value, but does return a `higher_score`
boolean. This is the value that is returned when the confidence is low."""


ALIASES: Final[dict[str, str]] = {
    "windows-874": "cp874",
}
"""Python prefers to use "cpXXX" for legacy encodings, while :code:`encoding_rs`
and :code:`chardetng` use whatwg names.

References
----------
https://docs.python.org/3/library/codecs.html#standard-encodings
https://encoding.spec.whatwg.org/#legacy-single-byte-encodings
"""
