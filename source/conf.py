# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Microbial Genomics Lab Spring 2022'
copyright = '2022, Jimmy Saw'
author = 'Jimmy Saw'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'nbsphinx'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
#html_theme = 'sphinx_rtd_theme'
#html_theme = 'haiku'

## cloud_sptheme (options: cloud, greencloud, magenta_cloud, redcloud, solarcloud)
from cloud_sptheme import themes
#html_theme = 'cloud'
html_theme = 'greencloud'
#html_theme = 'redcloud'

## set pygments styles
#pygments_style = 'arduino'
#pygments_style = 'tango'
#pygments_style = 'trac'
#pygments_style = 'friendly'
#pygments_style = 'autumn'
#pygments_style = 'solarized-light'
#pygments_style = 'xcode'
#pygments_style = 'paraiso-light'
pygments_style = 'lovelace'
#pygments_style = 'stata'
#pygments_style = 'vs'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_logo = 'gm_pan.png'

