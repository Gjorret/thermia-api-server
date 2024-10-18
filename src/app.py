from flask import Flask, Response
from prometheus_client import generate_latest
from src.prometheus_metrics import collect_data, custom_registry
from src.api import set_temperature

app = Flask(__name__)


@app.route('/metrics')
def metrics():
    collection_status = collect_data()
    if collection_status:
        return Response(collection_status, status=500, mimetype='text/plain')
    return Response(generate_latest(custom_registry), mimetype='text/plain')


@app.route('/api/temperature/set/<int:temperature>', methods=['POST'])
def set_temperature_endpoint(temperature):
    result = set_temperature(temperature)
    if result is not None:
        # If there is an error, return HTTP 500 with the error message
        return Response(result, status=500, mimetype='text/plain')
    # If successful, return HTTP 200 with a success message
    return Response(f'Temperature set to {temperature} degrees.', status=200, mimetype='text/plain')
