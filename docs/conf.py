import sphinx_material

# Register the theme as an extension to generate a sitemap.xml
# extensions.append('sphinx_material')
from recommonmark.parser import CommonMarkParser

source_parsers = {
    '.md': CommonMarkParser,
}
project = "Il Mare"
release = ''

author = u'Alessia Pagano - III C'

show_authors = True
# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('index', 'Mare.tex', project, author, 'manual'),
]
latex_elements = {
    'extraclassoptions': 'openany,oneside',
    'releasename': 'IC22 "Alberto Mario" - A.S. 2022/2023'
}
epub_basename = u'Mare'
# Choose the material theme
html_theme = 'sphinx_material'
#html_theme = 'sphinx_materialdesign_theme'
# Get the them path
html_theme_path = sphinx_material.html_theme_path()
# Register the required helpers for the html context
html_context = sphinx_material.get_html_context()
copyright = "2023 Alessia Pagano"
html_show_sourcelink = False
html_favicon = "favicon.ico"
html_logo = "logo.jpeg"
latex_logo = 'logo.jpeg'
html_title = "Home"
smartquotes = False
language = "it"
# The master toctree document.
master_doc = 'index'
source_suffix = ['.rst','.md']
html_sidebars = {
    '**': ['localtoc.html', 'globaltoc.html', 'sourcelink.html', 'searchbox.html']
}
# These folders are copied to the documentation's HTML output
html_static_path = ['_static']
templates_path = ['_templates']
# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/extra.css',
    'css/hacks.css',
    'css/material.css'
]
extensions = [
    'sphinxcontrib.images',
    "sphinx.ext.autodoc",
    "numpydoc",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "nbsphinx",
    "sphinx_markdown_tables",
    'sphinx.ext.githubpages'
]
html_theme_options = {
    'base_url': 'https://alessiapagano.github.io/tesina',
    'repo_url': 'https://github.com/alessiapagano/tesina/',
    'repo_name': 'alessiapagano/tesina',
    'nav_title': "Il Mare",
    'html_minify': True,
    'css_minify': True,
    'version_dropdown': False,
    'globaltoc_depth': 5,
    # Set the color and the accent color
    'color_primary': 'indingo',
    'color_accent': 'light-blue'
}
