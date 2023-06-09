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

## Installation

You can install _chardetng_py_ via [pip] from [PyPI]:

```console
$ pip install chardetng-py
```

Or via poetry:

```console
$ poetry add chardetng-py
```

## Usage

The easiest way to get started is to use the `decode` method.

```python

>>> import chardetng_py
>>> chardetng_py.decode(b'Jakby r\xeaka Boga')
'Jakby rêka Boga'
```

There is also a `detect` method available for compatability with `chardet`,
but it will always report `None` for the language and a confidence value of `0.99`.

```python

>>> from chardetng_py.compat import detect
>>> detect(b'Jakby r\xeaka Boga')
{'encoding': 'cp1254', 'confidence': 0.99, 'language': None}
```

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [MIT license][license],
_chardetng_py_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

## Credits

This project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.

[@cjolowicz]: https://github.com/cjolowicz
[pypi]: https://pypi.org/
[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python
[file an issue]: https://github.com/john-parton/chardetng-py/issues
[pip]: https://pip.pypa.io/

<!-- github-only -->

[license]: https://github.com/john-parton/chardetng-py/blob/main/LICENSE
[contributor guide]: https://github.com/john-parton/chardetng-py/blob/main/CONTRIBUTING.md
[command-line reference]: https://chardetng-py.readthedocs.io/en/latest/usage.html
