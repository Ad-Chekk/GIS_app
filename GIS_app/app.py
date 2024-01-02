# app.py
from dash import Dash, html, dcc, callback, Output, Input
import json

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Hello from Plotly Dash 11Backgargargsend!"),
    html.Button("Send Data", id="send-data-button"),
    html.Div(id="output-data")
])

# Endpoint for providing data
@app.callback(
    Output("output-data", "children"),
    [Input("send-data-button", "n_clicks")]
)
def send_data(n_clicks):
    if n_clicks:
        # You can put your data generation logic here
        data = {'message': 'Data from Plotly Dash Backend'}
        return json.dumps(data)

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)
