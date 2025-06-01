Recipes
=======

These are some additional possible uses for chardetng_py.

If there’s sufficient interest, we can stabilise these and include them
in the main package.

Detect the encoding of a bytestring and return a CodecInfo object
-----------------------------------------------------------------

.. code:: python

   def detect_codec(
       byte_str: Union[bytes, bytearray], *, allow_utf8: bool = True
   ) -> codecs.CodecInfo:
       r"""Detect the encoding of byte_str and return a CodecInfo object.

       Parameters
       ----------
       byte_str : bytes or bytearray
           Input buffer to detect the encoding of.

       Examples
       --------
       >>> codec = detect_codec(b"Jakby r\xeaka Boga")
       >>> codec.name
       'cp1254'

       """

       return codecs.lookup(detect(byte_str, allow_utf8=allow_utf8))

Detect the encoding of a bytestring and return the decoded string
-----------------------------------------------------------------

.. code:: python

   def decode(
       byte_str: Union[bytes, bytearray],
       errors: Literal[
           "strict", "ignore", "replace", "backslashreplace", "surrogateescape"
       ] = "strict",
       *,
       allow_utf8: bool = True,
   ) -> str:
       r"""Detect the encoding of byte_str and return the decoded string.

       Parameters
       ----------
       byte_str : bytes or bytearray
           Input buffer to decode.
       errors: "strict" or "ignore" or "replace" or "backslashreplace" or "surrogateescape"
           Error handler to use. See [Python documentation](https://docs.python.org/3/library/codecs.html#error-handlers)

       Examples
       --------
       >>> decode(b"Jakby r\xeaka Boga")
       'Jakby rêka Boga'

       """
       return byte_str.decode(detect(byte_str, allow_utf8=allow_utf8), errors=errors)

Open a file, incrementally determine its encoding and return a TextIOWrapper
----------------------------------------------------------------------------

This is a neat trick that allows you to open a file and detect its
encoding with a fixed amount of memory. The other bindings I’ve found
don’t support this use-case and you end up having to read the entire
file into memory, which is a problem for huge files.

This also lets you directly pass a text file of unknown encoding to
csv.writer of csv.DictWriter, for example.

.. code:: python

   # Reads entire file
   # We could add support for reading to some fixed position
   def _detect_buffer(buffer: IO[bytes], *, allow_utf8: bool = True, **kwargs):
       cursor_initial_position = buffer.tell()

       encoding_detector = EncodingDetector()

       # Not sure this is the best chunk size?
       while chunk := buffer.read(io.DEFAULT_BUFFER_SIZE):
           encoding_detector.feed(chunk, last=False)

       encoding_detector.feed(b"", last=True)

       buffer.seek(cursor_initial_position)

       return io.TextIOWrapper(
           buffer,
           encoding=encoding_detector.guess(tld=None, allow_utf8=allow_utf8),
           **kwargs,
       )


   # Could be nice to have an async one as well
   # unfortunately async fs tools aren't in std lib
   @contextmanager
   def detect_open(
       file: Union[bytes, str, PathLike], mode: Literal["r", "rt"] = "r", **kwargs
   ):
       """Open a file and detect its encoding."""
       if mode not in {"r", "rt"}:
           raise NotImplemented("Only reading supported at the moment")
           # TODO Could support r+ and w+ modes of operation?

       # The whole point is that we're going to detect in
       if "encoding" in kwargs:
           raise ValueError

       with open(file, mode="rb", **kwargs) as f:
           yield _detect_buffer(f)
