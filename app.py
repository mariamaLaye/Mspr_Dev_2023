import json
from flask import Flask, render_template
import requests


app = Flask(__name__)


def get_all_datas():
    response = requests \
        .get("https://615f5fb4f7254d0017068109.mockapi.io/api/v1/customers/")
    data = response.json()
    return data

@app.route("/<id>")
def get_client_by_id(id):
    response = requests \
        .get(f'https://615f5fb4f7254d0017068109.mockapi.io/api/v1/customers/{id}')
    data = response.json()
    return data

@app.route("/<id>/products")
def get_product_client_id(id):
    customers_data = get_client_by_id(id)
    return json.dumps(customers_data["orders"])













if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')