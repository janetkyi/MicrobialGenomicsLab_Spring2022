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

project = 'Microbial Genomics Lab'
copyright = '2020, Jimmy Saw'
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
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
#html_theme = 'bizstyle'
#html_theme = 'pytorch_sphinx_theme'
#html_theme_path = ["/Users/jsaw/opt/miniconda3/lib/python3.7/site-packages/pytorch_sphinx_theme"]
#html_theme = 'haiku'
#html_theme = 'nature'
#html_theme = 'pyramid'
#html_theme = 'traditional'

## Typlog theme
#html_theme = 'sphinx_typlog_theme'
#import sphinx_typlog_theme
#html_theme_path = [sphinx_typlog_theme.get_path()]

## Maisie theme
#import maisie_sphinx_theme
#html_theme_path = maisie_sphinx_theme.html_theme_path()
#html_theme = 'maisie_sphinx_theme'
# Register the theme as an extension to generate a sitemap.xml
#extensions.append("maisie_sphinx_theme")
# Maisie theme options (see theme.conf for more information)
#html_theme_options = {
#   # Set the name of the project to appear in the sidebar
#    "project_nav_name": "Microbial Genomics Lab",
#}

## Press theme
#html_theme = "press"

## Jupyter theme
#from jupyter_sphinx_theme import *
#init_theme()

## sphinx-material theme
#html_theme = 'sphinx_material'

## mozilla_sphinx_theme
#import mozilla_sphinx_theme
#import os
#html_theme_path = [os.path.dirname(mozilla_sphinx_theme.__file__)]
#html_theme = 'mozilla'

## sphinx_theme_pd
#import sphinx_theme_pd
#html_theme = "sphinx_theme_pd"
#html_theme_path = [sphinx_theme_pd.get_html_theme_path()]

## stanford_theme
#import stanford_theme
#html_theme = "stanford_theme"
#html_theme_path = [stanford_theme.get_html_theme_path()]

#import sphinx_theme
#html_theme = "neo_rtd_theme"
#html_theme_path = [sphinx_theme.get_html_theme_path('neo-rtd-theme')]

## sphinx_drove_theme
#html_theme = 'sphinx_drove_theme'
#import sphinx_drove_theme
#html_theme_path = [sphinx_drove_theme.get_html_theme_path()]

## renku-sphinx-theme
#html_theme = 'renku'

## guzzle_sphinx_theme
#import guzzle_sphinx_theme
# Adds an HTML table visitor to apply Bootstrap table classes
#html_translator_class = 'guzzle_sphinx_theme.HTMLTranslator'
#html_theme_path = guzzle_sphinx_theme.html_theme_path()
#html_theme = 'guzzle_sphinx_theme'

# Register the theme as an extension to generate a sitemap.xml
#extensions.append("guzzle_sphinx_theme")

# Guzzle theme options (see theme.conf for more information)
#html_theme_options = {
    # Set the name of the project to appear in the sidebar
#    "project_nav_name": "JS",
#}

## cloud_sptheme (options: cloud, greencloud, magenta_cloud, redcloud, solarcloud)
from cloud_sptheme import themes
html_theme = 'cloud'

## EdX theme
#import os
#import edx_theme
#extensions = ['edx_theme', 'nbsphinx']
#html_theme = 'edx_theme'
#html_theme_path = [edx_theme.get_html_theme_path()]

## oe_sphinx_theme
#import oe_sphinx_theme
#html_theme = 'oe_sphinx'
#html_theme_path = [oe_sphinx_theme.get_theme_dir()]

## wild_sphinx_theme
#import wild_sphinx_theme
#html_theme = 'wild'
#html_theme_path = [wild_sphinx_theme.get_theme_dir()]

## yummy sphinx theme
#html_theme = "yummy_sphinx_theme"
#html_theme_path = ["_themes", ]

## t3SphinxThemeRtd
#import t3SphinxThemeRtd
#html_theme = "t3SphinxThemeRtd"
#html_theme_path = [t3SphinxThemeRtd.get_html_theme_path()]

## sphinxjp.themes.basicstrap
#extensions += ['sphinxjp.themes.basicstrap']
#html_theme = 'basicstrap'

## pydata
#html_theme = 'pydata_sphinx_theme'


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

## pygment style
pygments_style = 'arduino'
#pygments_style = 'sphinx'
#pygments_style = 'monokai'
#pygments_style = 'tango'
#pygments_style = 'trac'
#pygments_style = 'rainbow_dash'
#pygments_style = 'murphy'
#pygments_style = 'autumn'
#pygments_style = 'perldoc'
#pygments_style = 'colorful'
#pygments_style = 'friendly'
#pygments_style = 'solarized-light'
#pygments_style = 'gruvbox-dark'

## logo
#html_logo = 'gw_monogram_2c.png'
#html_logo = 'course_logo.png'
html_logo = 'gm_pan.png'
