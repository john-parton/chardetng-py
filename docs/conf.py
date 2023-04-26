"""Sphinx configuration."""  # noqa: INP001
project = "chardetng Python Module"
author = "John Parton"
copyright = "2023, John Parton"  # noqa: A001
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
    "numpydoc",
]
autodoc_typehints = "description"
html_theme = "furo"
