import typing

Buffer: typing.TypeAlias = bytes | bytearray

class EncodingDetector:
    def feed(
        self: typing.Self,
        buffer: Buffer,
        /,
        *,
        last: bool,
    ) -> bool: ...
    def guess(
        self: typing.Self,
        *,
        tld: bytes | None,
        allow_utf8: bool,
    ) -> str: ...
    def guess_assess(
        self: typing.Self,
        *,
        tld: bytes | None,
        allow_utf8: bool,
    ) -> tuple[str, bool]: ...
