"""Sphinx configuration."""  # noqa: INP001
project = "chardetng Python Module"
author = "John Parton"
copyright = "2023, John Parton"  # noqa: A001
extensions = [
    "sphinx_toolbox.more_autodoc",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "numpydoc",
]
autodoc_typehints = "description"
html_theme = "furo"
github_username = "john-parton"
github_repository = "chardetng-py"
