from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")
setup(
    name="dash-console-filter-plugin",
    version="0.1.1",
    install_requires=[
        "dash>=3.1.1",
    ],
    packages=["dash_console_filter_plugin"],
    author="CNFeffery",
    author_email="fefferypzy@gmail.com",
    description="A plugin to filter the error messages in the console of the browser for Dash applications using Dash Hooks.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CNFeffery/dash-console-filter-plugin",
)
