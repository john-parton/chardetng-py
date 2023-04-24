import typing
from functools import wraps
import asyncio

import difflib
import itertools as it

from anyio import Path
import click
from chardetng_py import decode

import charset_normalizer

T = typing.TypeVar("T")
P = typing.ParamSpec("P")


def _decode_charset_normalizer(data):
    d = charset_normalizer.detect(data)
    return data.decode(d["encoding"]), d["encoding"]


def _decode_chardetng_py(data):
    text, encoding, _mangled = decode(data)
    return text, encoding


def coro(f: typing.Callable[P, typing.Awaitable[T]]) -> typing.Callable[P, T]:
    @wraps(f)
    def wrapper(*args, **kwargs):
        return asyncio.run(f(*args, **kwargs))

    return wrapper


MAX_LINES_OF_DIFF = 50


def print_diff(a, b, max_lines=MAX_LINES_OF_DIFF):
    diffs = difflib.ndiff(a.splitlines(), b.splitlines())

    for line in it.islice(diffs, max_lines):
        print(line, end="")


@click.command()
@click.option("--input-directory", "-i", type=click.Path(path_type=Path), required=True)
@coro
async def main(*, input_directory: Path):
    total = 0
    num_agree = 0

    async for path in input_directory.rglob("*"):
        if await path.is_file():
            async with await path.open("rb") as f:
                data = await f.read()

            total += 1

            (
                charset_normalizer_text,
                charset_normalizer_encoding,
            ) = _decode_charset_normalizer(data)
            (charsetng_py_text, charsetng_py_encoding) = _decode_chardetng_py(data)

            if charset_normalizer_text != charsetng_py_text:
                print_diff(charset_normalizer_text, charsetng_py_text)

                print(
                    f"Found files which decode differently between charsetng_py and charset_normalizer: {path}"
                )
                print(f"charset_normalizer reports: {charset_normalizer_encoding}")
                print(f"charsetng_py reports: {charsetng_py_encoding}")
                print(f"Total checked: {total}")
                print(f"Percentage agreeing so far {100 * num_agree / total}")

            else:
                num_agree += 1

                if total % 100 == 0:
                    print(f"Total checked: {total}")
                    print(f"Percentage agreeing so far {100 * num_agree / total}")


if __name__ == "__main__":
    main()
