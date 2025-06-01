chardetng_py
============

|PyPI| |Status| |Python Version| |License|

|Read the documentation at https://chardetng-py.readthedocs.io/| |Tests|

|pre-commit| |Black|

Features
--------

Python binding for the
`chardetng <https://github.com/hsivonen/chardetng>`__ character encoding
detector.

Installation
------------

You can install ``chardetng_py`` via `pip <https://pip.pypa.io/>`__ from
`PyPI <https://pypi.org/>`__:

.. code:: console

   $ pip install chardetng-py

Or via poetry:

.. code:: console

   $ poetry add chardetng-py

Quick Start
-----------

The easiest way to get started is to use the :meth:``detect`` method.

.. code:: python

   >>> from chardetng_py import detect
   >>> detect(b'Jakby r\xeaka Boga')
   'windows-1254'

There is also a ``detect`` method available for compatability with
``chardet``, but it will always report ``None`` for the language and a
confidence value of ``0.99``.

.. code:: python

   >>> from chardetng_py.compat import detect
   >>> detect(b'Jakby r\xeaka Boga')
   {'encoding': 'windows-1254', 'confidence': 0.99, 'language': None}

Contributing
------------

Contributions are very welcome. To learn more, see the `Contributor
Guide <https://github.com/john-parton/chardetng-py/blob/main/CONTRIBUTING.md>`__.

License
-------

Distributed under the terms of the `MIT
license <https://github.com/john-parton/chardetng-py/blob/main/LICENSE>`__,
``chardetng_py`` is free and open source software.

Issues
------

If you encounter any problems, please `file an
issue <https://github.com/john-parton/chardetng-py/issues>`__ along with
a detailed description.

Credits
-------

.. raw:: html

   <!-- github-only -->

.. |PyPI| image:: https://img.shields.io/pypi/v/chardetng-py.svg
   :target: https://pypi.org/project/chardetng-py/
.. |Status| image:: https://img.shields.io/pypi/status/chardetng-py.svg
   :target: https://pypi.org/project/chardetng-py/
.. |Python Version| image:: https://img.shields.io/pypi/pyversions/chardetng-py
   :target: https://pypi.org/project/chardetng-py
.. |License| image:: https://img.shields.io/pypi/l/chardetng-py
   :target: https://github.com/john-parton/chardetng-py/blob/main/LICENSE
.. |Read the documentation at https://chardetng-py.readthedocs.io/| image:: https://img.shields.io/readthedocs/chardetng-py/latest.svg?label=Read%20the%20Docs
   :target: https://chardetng-py.readthedocs.io/
.. |Tests| image:: https://github.com/john-parton/chardetng-py/workflows/Tests/badge.svg
   :target: https://github.com/john-parton/chardetng-py/actions?workflow=Tests
.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black

.. toctree::
    :maxdepth: 0
    :hidden:

    usage
    shortcuts
    class_reference
    recipes
