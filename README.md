# chardetng-py
Simple python binding for rust charsetng library

## Usage

The only function exposed by the library is `decode`. The only argument is a `bytes` object.

Returns a tuple of `str`.

```python

>>> import chardetng_py
>>> chardetng_py.decode(b'Jakby r\xeaka Boga')
'Jakby rêka Boga'
```

## Performance

In my basic testing, chardetng is about 40-80 times faster than `chardet` or `charset_normalizer`. (That's 4,000% - 8,000%). See `bench.py` for some example benchmarking code.

## Accuracy

I chardetng and charset_normalizer agree about 70% of the time with an ML dataset I'm working on. The 30% of the time when they disagree, chardetng's encoding is almost always the correct one. [Blog post by Henri Sivonen, Mozilla Foundation](https://hsivonen.fi/chardetng/)


## Acknowledgements

When I started work on this project, I could not find any python bindings for chardetng, so I decided to make one. Looks like emmattiza had the [same idea](https://github.com/emattiza/rs_chardet)

The biggest difference is this library decodes the string using `encoding_rs`, whereas rs_chardet requires you to decode the string in python. It turns out not to matter that much in most cases. On my machine, they're almost exactly the same performance, but it will depend on your CPU architecture, Python version, age of the CPU and a bunch of other variables.