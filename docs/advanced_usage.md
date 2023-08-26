# Advanced Usage

The easiest way to get started is to use the :meth:`decode` method.

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
