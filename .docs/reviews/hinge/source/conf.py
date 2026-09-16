"""Sphinx configuration for the hinge review."""

project = "The hinge"
copyright = "2026, Mike Stitt"
author = "Mike Stitt"
release = "2026-08-30"

extensions: list[str] = []
exclude_patterns = ["_build"]

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_title = "What is wrong with the hinge"
html_show_sphinx = False
html_copy_source = False
html_theme_options = {
    "collapse_navigation": False,
    "navigation_depth": 2,
    "prev_next_buttons_location": None,
}
