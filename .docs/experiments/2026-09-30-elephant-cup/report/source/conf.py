"""Sphinx configuration for the elephant cup conversation report."""

project = "elephant cup"
copyright = "2026, Mike Stitt"
author = "Mike Stitt"

extensions: list[str] = []
exclude_patterns = ["_build"]

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["report.css"]
html_title = "elephant cup, the conversation"
html_show_sphinx = False
html_show_sourcelink = False
html_copy_source = False
html_theme_options = {
    "collapse_navigation": False,
    "navigation_depth": 2,
    "prev_next_buttons_location": None,
}
