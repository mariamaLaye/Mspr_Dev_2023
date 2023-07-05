import json
import sqlite3 as sql
from flask import Flask
import requests
from db.CustomerDB import CustomerDB
from db.ProductDB import ProductDB

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

@app.route("/customers/<id>/")
def get_client_id(id):
    con = sql.connect("msprDev")
    customer_db = CustomerDB(None, con)
    customer_datas = customer_db.get_customer(id) 
    return customer_datas

@app.route("/customers")
def get_customers():
    con = sql.connect("msprDev")
    custome_db = CustomerDB(None, con)
    rows = custome_db.get_all_customers()    
    return rows

@app.route("/products")
def get_products():
    con = sql.connect('msprDev')
    product_db = ProductDB(None, con)
    rows = product_db.get_all_products() 
    return rows

@app.route("/products/<id>")
def get_product_by_id(id):
    con = sql.connect("msprDev")
    product_db = ProductDB(None, con)
    product_datas = product_db.get_product(id) 
    return product_datas

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')