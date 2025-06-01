Inform the detector of a chunk of input.

The byte stream is represented as a sequence of calls to this
method such that the concatenation of the arguments to this
method form the byte stream. It does not matter how the application
chooses to chunk the stream. It is OK to call this method with
a zero-length byte slice.

The end of the stream is indicated by calling this method with
:code:`last` set to :code:`True`. In that case, the end of the stream is
considered to occur after the last byte of the :code:`buffer` (which
may be zero-length) passed in the same call. Once this method
has been called with :code:`last` set to :code:`True` this method must not
be called again.

If you want to perform detection on just the prefix of a longer
stream, do not pass :code:`last=True` after the prefix if the stream
actually still continues.

Returns :code:`True` if after processing :code:`buffer` the stream has
contained at least one non-ASCII byte and :code:`False` if only
ASCII has been seen so far.

## Parameters

buffer : :code:`bytes` or :code:`bytearray`
The next chunk of the byte stream.
last : :code:`bool`
Whether this is the last chunk of the byte stream.

## Returns

:code:`bool`
:code:`True` if the stream has contained at least one non-ASCII byte
and :code:`False` if only ASCII has been seen so far.

## Raises

pyo3_runtime.PanicException
If this method has previously been called with :code:`last` set to :code:`True`.
