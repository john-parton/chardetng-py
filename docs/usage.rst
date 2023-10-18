Usage
=====

Basic Usage
-----------

The easiest way to get started is to use the ``detect`` method.

.. code:: python

   >>> from chardetng_py import detect
   >>> detect(b'Jakby r\xeaka Boga')
   'windows-1254'

There is also a ``detect`` method available for compatability with
``chardet``, but it will always report ``None`` for the language. The confidence
value will either be ``0.99`` or ``0.01`` depending on whether chardetng returns
a "high" or "low" confidence flag.

.. code:: python

   >>> from chardetng_py.compat import detect
   >>> detect(b'Jakby r\xeaka Boga')
   {'encoding': 'windows-1254', 'confidence': 0.99, 'language': None}

Advanced Usage
--------------

It is also possible to use the ``EncodingDetector`` class directly.

.. code:: python

   >>> from chardetng_py import EncodingDetector
   >>> detector = EncodingDetector()
   >>> detector.feed(b'Jakby r\xeaka Boga', last=True)
   >>> detector.guess(tld=None, allow_utf8=True)
   'windows-1254'
