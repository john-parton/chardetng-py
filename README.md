# chardetng-py
Simple python binding for rust charsetng library

## Usage

The only function exposed by the library is `decode`. The only argument is a `bytes` object.

Returns a tuple of `(decoded_text, detected encoding, had_errors)`.

```python

>>> import chardetng_py
>>> chardetng_py.decode(b'Jakby r\xeaka Boga')
('Jakby rêka Boga', 'windows-1254', False)
```

## Performance

In my basic testing, chardetng is about 40-80 times faster than `chardet` or `charset_normalizer`. (That's 4,000% - 8,000%). See `bench.py` for some example benchmarking code.

## Accuracy

`TODO`
