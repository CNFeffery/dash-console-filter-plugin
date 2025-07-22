# dash-console-filter-plugin

[![GitHub](https://shields.io/badge/license-MIT-informational)](https://github.com/CNFeffery/dash-console-filter-plugin/blob/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/dash-console-filter-plugin.svg?color=dark-green)](https://pypi.org/project/dash-console-filter-plugin/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

English | [简体中文](./README-zh_CN.md)

Console message filtering plugin for Dash applications using Dash Hooks. This plugin allows you to filter specific error messages in the browser console.

## Installation

```bash
pip install dash-console-filter-plugin
```

## Usage

```python
import dash

# Import the console filter plugin
from dash_console_filter_plugin import setup_console_filter_plugin

# Enable the console filter plugin for the current app
setup_console_filter_plugin(keywords=["test warning message"])

app = dash.Dash(__name__)

# Rest of your app code...
```

## Example

Run the included example:

```bash
python example.py
```

<center><img src="./images/demo.gif" /></center>

## API Reference

### `setup_console_filter_plugin()`

This function enables the console message filtering feature for your Dash application.

| Parameter  | Type      | Default | Description                                                                                                           |
| ---------- | --------- | ------- | --------------------------------------------------------------------------------------------------------------------- |
| `keywords` | List[str] | None    | List of keywords to filter, messages containing any of these keywords in the console of the browser will be filtered. |
