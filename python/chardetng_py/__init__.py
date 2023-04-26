"""Functions for dealing with byte strings of unknown encoding."""

from chardetng_py.api import decode, detect, detect_codec

# Documentation for the detect function is on the rust function
# in lib.rs

__all__: list[str] = [
    "detect",
    "detect_codec",
    "decode",
]
