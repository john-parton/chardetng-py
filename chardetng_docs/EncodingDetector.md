A Web browser-oriented detector for guessing what character
encoding a stream of bytes is encoded in.

The bytes are fed to the detector incrementally using the `feed`
method. The current guess of the detector can be queried using
the `guess` method. The guessing parameters are arguments to the
`guess` method rather than arguments to the constructor in order
to enable the application to check if the arguments affect the
guessing outcome. (The specific use case is to disable UI for
re-running the detector with UTF-8 allowed and the top-level
domain name ignored if those arguments don't change the guess.)
