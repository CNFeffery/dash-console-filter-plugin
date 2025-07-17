import dash
from dash import html

# Import the console filter plugin
from dash_console_filter_plugin import setup_console_filter_plugin

# Enable the console filter plugin for the current app
setup_console_filter_plugin(keywords=["demo message"])

app = dash.Dash(__name__)

app.layout = html.Div("Test App.", style={"padding": 50})

if __name__ == "__main__":
    app.run()
