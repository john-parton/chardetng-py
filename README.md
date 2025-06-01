# chardetng_py

[![PyPI](https://img.shields.io/pypi/v/chardetng-py.svg)][pypi_]
[![Status](https://img.shields.io/pypi/status/chardetng-py.svg)][status]
[![Python Version](https://img.shields.io/pypi/pyversions/chardetng-py)][python version]
[![License](https://img.shields.io/pypi/l/chardetng-py)][license]

[![Read the documentation at https://chardetng-py.readthedocs.io/](https://img.shields.io/readthedocs/chardetng-py/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/john-parton/chardetng-py/workflows/Tests/badge.svg)][tests]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi_]: https://pypi.org/project/chardetng-py/
[status]: https://pypi.org/project/chardetng-py/
[python version]: https://pypi.org/project/chardetng-py
[read the docs]: https://chardetng-py.readthedocs.io/
[tests]: https://github.com/john-parton/chardetng-py/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/john-parton/chardetng-py
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

## Features

Python binding for the [chardetng](https://github.com/hsivonen/chardetng) character encoding detector.

## Documentation

Documentation for the latest release can be found on [Read the Docs](https://chardetng-py.readthedocs.io/en/latest/).

## Platform and Architecture Support

Compatability is a _feature_ of `chardetng_py`. The goal is to support as many platforms and architectures as possible.

`chardetng_py` supports Python 3.8, 3.9, 3.10, 3.11, and 3.12 on Linux, macOS 10.7, macOS 11.0, and Windows. Additionally, PyPy versions 3.8, 3.9, and 3.10 are supported on Linux.

The x86, x86_64, s390x, ARMv7l, and AArch64 architectures are supported on Linux for both cPython and PyPy. The AArch64 and x86_64 architectures are supported on macOS. The x86_64 architecture is supported on Windows.

In short, if you can install Python 3.8, you should be able to install `chardetng_py`.

If there is a platform or architecture that you would like to see supported, please [file an issue].

This support is largely due to the wonderful [maturin](https://github.com/PyO3/maturin) project.

## Installation

You can install `chardetng_py` via [pip] from [PyPI]:

```console
$ pip install chardetng-py
```

Or via poetry:

```console
$ poetry add chardetng-py
```

## Quick Start

The easiest way to get started is to use the :meth:`detect` method.

```python
>>> from chardetng_py import detect
>>> detect(b'Jakby r\xeaka Boga')
'windows-1254'
```

There is also a `detect` method available for compatability with `chardet`,
but it will always report `None` for the language. The confidence value will either
be `0.99` or `0.01` depending on whether chardetng returns a "high" or "low"
confidence boolean.

```python
>>> from chardetng_py.compat import detect
>>> detect(b'Jakby r\xeaka Boga')
{'encoding': 'windows-1254', 'confidence': 0.99, 'language': None}
```

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [MIT license][license],
`chardetng_py` is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

## Credits

[pypi]: https://pypi.org/
[file an issue]: https://github.com/john-parton/chardetng-py/issues
[pip]: https://pip.pypa.io/

<!-- github-only -->

[license]: https://github.com/john-parton/chardetng-py/blob/main/LICENSE
[contributor guide]: https://github.com/john-parton/chardetng-py/blob/main/CONTRIBUTING.md
[command-line reference]: https://chardetng-py.readthedocs.io/en/latest/usage.html
