import codecs
import typing

from chardetng_py._rust import detect


def detect_codec(input: bytes) -> codecs.Codec:
    # I'm not sure chardetng will return a value here that python doesn't understand
    # I'm pretty sure it *won't*, but if it does, this will raise codecs.LookpError
    return codecs.lookup(detect(input))


def decode(input: bytes) -> str:
    """
    Detect the encoding of input, and decode.

    Returns the decoded string.
    """
    return detect_codec(input).decode(input)
