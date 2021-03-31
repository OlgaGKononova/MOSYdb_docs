# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
# sys.path.insert(0, os.path.abspath('.'))
#sys.path.append(os.path.join(os.environ["SAMPLE_DOCS_LOCATION"], "demo"))
#print("", sys.path[-1], "", sep="\n" + "-" * 80 + "\n")


# -- Project information -----------------------------------------------------

project = 'MOSYdb Documentation'
copyright = '2021, Olga Kononova & Yevgeny Rakita Shlafstein'
author = 'Olga Kononova & Yevgeny Rakita Shlafstein'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_css_files = [
#    'css/insegel_upd.css',
#]
html_theme = 'insegel'
html_logo = "MOSYdb.png"
html_favicon = "MOSYdb-32.png"
html_theme_options = {
    'display_version': False,
    'wending_last_updated' : False
}
html_show_sphinx = False
