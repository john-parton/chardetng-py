"""Functions for dealing with byte strings of unknown encoding.

All of the functions in this module are re-imported in the top-level
chardetng_py module.
"""

import codecs
import typing

from chardetng_py._rust import EncodingDetector

ALIASES: dict[str, str] = {
    "windows-874": "cp874",
}
"""
Python prefers to use "cpXXX" for legacy encodings, while encoding_rs
(and by extension chardetng) use whatwg

References
----------

https://docs.python.org/3/library/codecs.html#standard-encodings
https://encoding.spec.whatwg.org/#legacy-single-byte-encodings
"""


def detect(byte_str: typing.Union[bytes, bytearray]) -> str:
    """Detect the encoding of byte_str and return the encoding.

    Parameters
    ----------
    byte_str : bytes or bytearray
        Input buffer to decode.

    Returns
    -------
        str
    The decoded string.
    """
    encoding_detector = EncodingDetector()
    encoding_detector.feed(byte_str, last=True)

    encoding: str = encoding_detector.guess(tld=None, allow_utf8=True)

    # chardetng uses 'windows-874' as an encoding, which Python does not understand
    # I believe that windows-874 and cp874 are basically the same encoding
    if encoding in ALIASES:
        # TODO Log/warn?
        return ALIASES[encoding]

    return encoding


def detect_codec(byte_str: typing.Union[bytes, bytearray]) -> codecs.CodecInfo:
    r"""Detect the encoding of byte_str and return a CodecInfo object.

    Parameters
    ----------
    byte_str : bytes or bytearray
        Input buffer to detect the encoding of.

    Examples
    --------
    >>> codec = detect_codec(b"Jakby r\xeaka Boga")
    >>> codec.name
    'cp1254'

    """
    encoding_detector = EncodingDetector()
    encoding_detector.feed(byte_str, last=True)

    encoding_detector.guess(tld=None, allow_utf8=True)

    return codecs.lookup(detect)


def decode(
    byte_str: typing.Union[bytes, bytearray],
    errors: typing.Union[
        typing.Literal["strict"],
        typing.Literal["ignore"],
        typing.Literal["replace"],
        typing.Literal["backslashreplace"],
        typing.Literal["surrogateescape"],
    ] = "strict",
) -> str:
    r"""Detect the encoding of byte_str and return the decoded string.

    Parameters
    ----------
    byte_str : bytes or bytearray
        Input buffer to decode.
    errors: "strict" or "ignore" or "replace" or "backslashreplace" or "surrogateescape"
        Error handler to use. See [Python documentation](https://docs.python.org/3/library/codecs.html#error-handlers)

    Examples
    --------
    >>> decode(b"Jakby r\xeaka Boga")
    'Jakby rêka Boga'

    """
    return byte_str.decode(detect(byte_str), errors=errors)
