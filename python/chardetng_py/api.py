"""Functions for dealing with byte strings of unknown encoding.

All of the functions in this module are re-imported in the top-level
chardetng_py module.
"""

import codecs
import typing

from chardetng_py._rust import detect


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
    # I'm not sure chardetng will return a value here that python doesn't understand
    # I'm pretty sure it *won't*, but if it does, this will raise codecs.LookpError
    return codecs.lookup(detect(byte_str))


def decode(byte_str: typing.Union[bytes, bytearray]) -> str:
    r"""Detect the encoding of byte_str and return the decoded string.

    Parameters
    ----------
    byte_str : bytes or bytearray
        Input buffer to decode.

    Examples
    --------
    >>> decode(b"Jakby r\xeaka Boga")
    'Jakby rêka Boga'

    """
    return byte_str.decode(detect(byte_str))
