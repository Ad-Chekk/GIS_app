from flask import Flask, send_from_directory
from dash import Dash, html
import json

# Flask app for the proxy server
proxy_app = Flask(__name__)

# Serve the JavaScript frontend
@proxy_app.route('/assets/test.html')
def serve_frontend():
    return send_from_directory('.', 'test.html')

# Plotly Dash app
dash_app = Dash(__name__, server=proxy_app)

dash_app.layout = html.Div("Hello from Plotly Dash Backend!")

if __name__ == '__main__':
    # Run both Flask (proxy server) and Plotly Dash app together
    dash_app.run_server(debug=True, use_reloader=False)
