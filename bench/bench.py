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

T = typing.TypeVar("T")
P = typing.ParamSpec("P")

def test_chardet(data):
    for datum in data:
        d = chardet.detect(datum)

        datum.decode(d["encoding"], errors="replace")

def test_charset_normalizer(data):
    for datum in data:
        d = charset_normalizer.detect(datum)
        print(d["encoding"])

        datum.decode(d["encoding"])

def test_chardetng_py(data):
    for datum in data:
        __, encoding, __ = decode(datum)


def coro(f: typing.Callable[P, typing.Awaitable[T]]) -> typing.Callable[P, T]:
    @wraps(f)
    def wrapper(*args, **kwargs):
        return asyncio.run(f(*args, **kwargs))

    return wrapper


@click.command()
@click.option("--input-directory", "-i", type=click.Path(path_type=Path), required=True)
@click.option("--sample-size", "-k", type=int, help="Number of files to read into memory for benchmarks.", default=10)
@click.option("--iterations", "-n", type=int, help="Number of iterations of timeit to run.", default=10)
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
        test_chardet,
        test_chardetng_py,
        test_charset_normalizer,
    ]

    random.shuffle(test_functions)

    for test_function in test_functions:
        loops, total_time = Timer("test_func(data)", globals={"test_func": test_function, "data": data}).autorange()

        print(test_function.__name__, loops, total_time / loops)

if __name__ == "__main__":
    main()