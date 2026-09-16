"""Sphinx configuration for the robot build, draft9p2."""

project = "Robot in Onshape"
copyright = "2026, Mike Stitt"
author = "Mike Stitt"
release = "draft9p4"

extensions: list[str] = []
exclude_patterns = ["_build"]

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_title = "Building the robot"
html_show_sphinx = False
html_copy_source = False
html_theme_options = {
    "collapse_navigation": False,
    "navigation_depth": 2,
    "prev_next_buttons_location": None,
}
