import random
import typing
from functools import wraps
import asyncio

from anyio import Path
import click
from timeit import Timer
from chardetng_py import decode

import charset_normalizer
import chardet
import rs_chardet

T = typing.TypeVar("T")
P = typing.ParamSpec("P")

def test_chardet(data):
    for datum in data:
        d = chardet.detect(datum)

        datum.decode(d["encoding"], errors="replace")

def test_charset_normalizer(data):
    for datum in data:
        d = charset_normalizer.detect(datum)
        datum.decode(d["encoding"])

def test_chardetng_py(data):
    for datum in data:
        decode(datum)

def test_chardetng_py_info(data):
    for datum in data:
        __, encoding, __ = decode_info(datum)

def test_rs_chardet(data):
    for datum in data:
        codec = rs_chardet.detect_codec(datum)
        codec.decode(datum)


def coro(f: typing.Callable[P, typing.Awaitable[T]]) -> typing.Callable[P, T]:
    @wraps(f)
    def wrapper(*args, **kwargs):
        return asyncio.run(f(*args, **kwargs))

    return wrapper


@click.command()
@click.option("--input-directory", "-i", type=click.Path(path_type=Path), required=True)
@click.option("--sample-size", "-k", type=int, help="Number of files to read into memory for benchmarks.", default=200)
@click.option("--iterations", "-n", type=int, help="Number of iterations of timeit to run.", default=12)
@coro
async def main(*, input_directory: Path, sample_size: int, iterations: int):

    paths = []

    async for path in input_directory.rglob("*"):
        if await path.is_file():
            paths.append(path)

            if len(paths) == sample_size:
                break 

    async def _read(path):
        async with await path.open("rb") as f:
            return await f.read()
        
    data = await asyncio.gather(*[_read(path) for path in paths])

    print("Done fetching data")

    test_functions = [
        # test_chardet,
        test_chardetng_py,
        # test_charset_normalizer,
        test_rs_chardet,
    ]

    random.shuffle(test_functions)

    for test_function in test_functions:
        total_time = Timer("test_func(data)", globals={"test_func": test_function, "data": data}).timeit(number=iterations)

        print(test_function.__name__, iterations, total_time / iterations)

if __name__ == "__main__":
    main()