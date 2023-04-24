import typing

from chardetng_py.api import detect_codec


if typing.TYPE_CHECKING:
    # TypedDict was introduced in Python 3.8.
    #
    # TODO: Remove the else block and TYPE_CHECKING check when dropping support
    # for Python 3.7.

    class ResultDict(typing.TypedDict):
        encoding: typing.Optional[str]
        confidence: float
        language: typing.Optional[str]

else:
    ResultDict = dict

# chardetng does not return a confidence value
# This is the value which is unconditionally returned
DEFAULT_CONFIDENCE: typing.Final[float] = 0.99


def detect(input: bytes) -> ResultDict:
    """
    chardet legacy method
    Detect the encoding of the given byte string. It may or may not be backward-compatible.
    This function is primarily used to migrate from chardet or charset_normalizer.
    """

    return {
        "encoding": detect_codec(input).name,
        "confidence": DEFAULT_CONFIDENCE,
        # chardetng does not return a language
        "language": None,
    }
