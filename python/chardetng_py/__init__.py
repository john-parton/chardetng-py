"""Functions for dealing with byte strings of unknown encoding.".

:code:`detect` is imported from :code:`chardetng_py.api` and so therefore may
be imported using :code:`from chardetng_py import detect`.
"""

from typing import Final, List

from chardetng_py.detector import EncodingDetector
from chardetng_py.shortcuts import detect

# Documentation for the detect function is on the rust function
# in lib.rs

__all__: Final[List[str]] = [
    "detect",
    "EncodingDetector",
]
