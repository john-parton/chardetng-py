Guess the encoding given the bytes pushed to the detector so far
(via :code:`feed()`), the top-level domain name from which the bytes were
loaded, and an indication of whether to consider UTF-8 as a permissible
guess.

## Parameters

tld : :code:`bytes` or :code:`bytearray` or :code:`None`
The rightmost DNS label of the hostname of the
host the stream was loaded from in lower-case ASCII form. That is, if
the label is an internationalized top-level domain name, it must be
provided in its Punycode form. If the TLD that the stream was loaded
from is unavalable, :code:`None` may be passed instead, which is equivalent
to passing :code:`b"com"`.
allow_utf8 : :code:`bool`
If set to :code:`False`, the return value of
this method won't be :code:`"UTF-8"`. When performing detection
on :code:`text/html` on non-:code:`file:` URLs, Web browsers must pass
:code:`False`, unless the user has taken a specific contextual action to request an
override. This way, Web developers cannot start depending on UTF-8
detection. Such reliance would make the Web Platform more brittle.

## Returns

:code:`str`
The guessed encoding.

## Raises

pyo3_runtime.PanicException
If :code:`tld` contains non-ASCII, period, or upper-case letters. The exception
condition is intentionally limited to signs of failing to extract the
label correctly, failing to provide it in its Punycode form, and failure
to lower-case it. Full DNS label validation is intentionally not performed
to avoid panics when the reality doesn't match the specs.
