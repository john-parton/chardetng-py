Inform the detector of a chunk of input.

The byte stream is represented as a sequence of calls to this
method such that the concatenation of the arguments to this
method form the byte stream. It does not matter how the application
chooses to chunk the stream. It is OK to call this method with
a zero-length byte slice.

The end of the stream is indicated by calling this method with
`last` set to `True`. In that case, the end of the stream is
considered to occur after the last byte of the `buffer` (which
may be zero-length) passed in the same call. Once this method
has been called with `last` set to `True` this method must not
be called again.

If you want to perform detection on just the prefix of a longer
stream, do not pass `last=true` after the prefix if the stream
actually still continues.

Returns `True` if after processing `buffer` the stream has
contained at least one non-ASCII byte and `False` if only
ASCII has been seen so far.

## Parameters

buffer : bytes or bytearray
last : bool

## Returns

bool
`True` if the stream has contained at least one non-ASCII byte
and `False` if only ASCII has been seen so far.

## Raises

pyo3_runtime.PanicException
If this method has previously been called with `last` set to `True`.
