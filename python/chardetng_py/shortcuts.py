"""Functions for dealing with byte strings of unknown encoding."""

from __future__ import annotations

from chardetng_py.detector import EncodingDetector


def detect(
    byte_str: bytes | bytearray,
    *,
    allow_utf8: bool = False,
    tld: bytes | bytearray | None = None,
) -> str:
    """Detect the encoding of :code:`byte_str`.

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
    tld : :code:`bytes` or :code:`bytearray` or :code:`None`
        If :code:`tld` contains non-ASCII, period, or upper-case letters. The exception
        condition is intentionally limited to signs of failing to extract the
        label correctly, failing to provide it in its Punycode form, and failure
        to lower-case it. Full DNS label validation is intentionally not performed
        to avoid panics when the reality doesn't match the specs.

    Returns
    -------
    :code:`str`
    The encoding of :code:`byte_str`, suitable for use with :code:`str.decode`.
    """
    encoding_detector = EncodingDetector()
    encoding_detector.feed(byte_str, last=True)

    return encoding_detector.guess(tld=tld, allow_utf8=allow_utf8)
