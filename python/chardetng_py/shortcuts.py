"""Functions for dealing with byte strings of unknown encoding."""

from typing import Dict, Final, Union

from chardetng_py.detector import EncodingDetector

ALIASES: Final[Dict[str, str]] = {
    "windows-874": "cp874",
}
"""Python prefers to use "cpXXX" for legacy encodings, while :code:`encoding_rs`
and :code:`chardetng` use whatwg names.

References
----------
https://docs.python.org/3/library/codecs.html#standard-encodings
https://encoding.spec.whatwg.org/#legacy-single-byte-encodings
"""


def detect(byte_str: Union[bytes, bytearray], *, allow_utf8: bool = False) -> str:
    """Detect the encoding of :code:`byte_str`.

    Returned encoding is suitable for use with :code:`str.decode`.

    Parameters
    ----------
    byte_str : :code:`bytes` or :code:`bytearray`
        Input buffer to decode.
    allow_utf8 : :code:`bool`
        If set to :code:`False`, the return value of
        this method won't be :code:`"UTF-8"`. When performing detection
        on :code:`"text/html"` on non-:code:`file:` URLs, Web browsers must pass
        :code:`False`,
        unless the user has taken a specific contextual action to request an
        override. This way, Web developers cannot start depending on UTF-8
        detection. Such reliance would make the Web Platform more brittle.
    """
    encoding_detector = EncodingDetector()
    encoding_detector.feed(byte_str, last=True)

    encoding: str = encoding_detector.guess(tld=None, allow_utf8=allow_utf8)

    # chardetng uses 'windows-874' as an encoding, which Python does not understand
    # I believe that windows-874 and cp874 are basically the same encoding
    if encoding in ALIASES:
        # TODO Log/warn?
        return ALIASES[encoding]

    return encoding
