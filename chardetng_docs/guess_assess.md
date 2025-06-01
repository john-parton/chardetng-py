Performs the same function as :code:`guess()` with the same parameters, but
additionally returns whether the guessed encoding had a higher score than
at least one other candidate. If this method returns :code:`False`, the
guessed encoding is likely to be wrong.

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

encoding: :code:`str`
The guessed encoding.
higher_score: :code:`bool`
Whether the guessed encoding had a higher score than at least
one other candidate. If this value is :code:`False`, the guessed encoding
is likely to be wrong.

## Raises

pyo3_runtime.PanicException
If :code:`tld` contains non-ASCII, period, or upper-case letters. The exception
condition is intentionally limited to signs of failing to extract the
label correctly, failing to provide it in its Punycode form, and failure
to lower-case it. Full DNS label validation is intentionally not performed
to avoid panics when the reality doesn't match the specs.
