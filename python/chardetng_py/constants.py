"""Constants used by chardetng_py."""

from typing import Final

CONFIDENCE_HIGH: Final[float] = 0.99
"""chardetng does not return a confidence value, but does return a `higher_score`
boolean. This is the value that is returned when the confidence is high."""

CONFIDENCE_LOW: Final[float] = 0.01
"""chardetng does not return a confidence value, but does return a `higher_score`
boolean. This is the value that is returned when the confidence is low."""
