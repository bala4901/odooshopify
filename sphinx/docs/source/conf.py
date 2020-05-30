###############
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
import sphinx_rtd_theme


# -- Project information -----------------------------------------------------

project = 'Odoo Shopify Connector'
copyright = '2020, PT Solusi Otomasi Servis'
author = 'PT Solusi Otomasi Servis'

# The full version, including alpha/beta/rc tags
version = "1.0.0"
release = "1"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "recommonmark",
    "rst2pdf.pdfbuilder",
    "rinoh.frontend.sphinx",
    "sphinxcontrib.mermaid",
    "sphinx.ext.todo",
    "sphinx.ext.githubpages",
    "sphinx_rtd_theme",
    "sphinx.ext.autosectionlabel",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

source_suffix = ".rst"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_show_sourcelink = False
html_show_sphinx = False
html_theme_options = {
    "canonical_url": "",
    # 'analytics_id': 'UA-XXXXXXX-1',  #  Provided by Google in your dashboard
    "logo_only": False,
    "display_version": True,
    "prev_next_buttons_location": "bottom",
    "style_external_links": False,
    "style_nav_header_background": "#2980B9",
    # Toc options
    "collapse_navigation": True,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": True,
    "titles_only": True,
}
# html_logo = 'logo_html.png'

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = "%b %d, %Y"

mermaid_params = [
    "--theme",
    "forest",
    "--width",
    "600",
    "--backgroundColor",
    "transparent",
]

latex_logo = 'logo_side.png'


###################################
rinoh_documents = [
    (
        "index",  # top-level file (index.rst)
        "Automation Warehouse System for \nJ.CO. Donuts & Coffee",  # output (target.pdf)
        "JCO",  # document title
        "Markus Bala",
    )
]  # document author

############## RST2PDF #################
pdf_documents = [
    (
        "index",
        "jco",
        "Automation Warehouse System for \nJ.CO. Donuts & Coffee",  # output (target.pdf)
        "Markus Bala",
    )
]  # document author
# A comma-separated list of custom stylesheets. Example:
# stylesheets="fruity.json,a4paper.json,verasans.json"

# pdf_stylesheets = ["manual"]

# Create a compressed PDF
# Use true/false (lower case) or 1/0
pdf_compressed = False

# A list of folders to search for stylesheets. Example:
pdf_style_path = ['~/project/src/jco/source/styles']



pdf_blank_first_page = False
pdf_use_toc = True
pdf_use_numbered_links = True

# Page template name for "regular" pages
# pdf_page_template = 'cutePage'

# Cover page template.
# It will be searched in the document's folder, in ~/.rst2pdf/templates and
# in the templates subfolder of the package folder

pdf_cover_page = 'sphinxcover.tmpl'