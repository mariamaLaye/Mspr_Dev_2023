import json
import sqlite3 as sql
from flask import Flask, request
import requests
from db.CustomerDB import CustomerDB, json_to_customer
from db.OrderDB import OrderDB
from db.ProductDB import ProductDB, json_to_product


app = Flask(__name__)

def get_all_data(data_type):
    response = requests \
        .get(f"https://615f5fb4f7254d0017068109.mockapi.io/api/v1/{data_type}/")
    data = response.json()
    return data

def get_bytes_to_json(bytes):
    json_val = bytes.decode('utf8').replace("'", '"')
    data = json.loads(json_val)
    return data

# Customer methods
@app.route("/customers/", methods=["GET"])
def get_customers():
    con = sql.connect("msprDev")
    customer_db = CustomerDB(con)
    rows = customer_db.get_all_customers()   
    con.close() 
    return rows

@app.route("/customers/<id>/", methods=["GET"])
def get_customer_by_id(id):
    con = sql.connect("msprDev")
    customer_db = CustomerDB(None, con)
    customer_datas = customer_db.get_customer_by_id(id) 
    con.close()
    return customer_datas

@app.route("/customer/add/", methods=["POST"])
def add_customer():
    data = request.data
    json_customer = get_bytes_to_json(data)
    
    con = sql.connect('msprDev')
    customer_db = CustomerDB(con)
    customer_db.add_customer(json_to_customer(json_customer))
    con.close()
    return json_customer

@app.route("/customers/update/", methods=["PUT"])
def update_customer():
    data = request.data
    json_customer = get_bytes_to_json(data)
    
    con = sql.connect('msprDev')
    customer_db = CustomerDB(con)
    customer = json_to_customer(json_customer)
    customer_db.update_customer(customer)
    con.close()
    return f"Customer with id : {customer.get_id} updated"

@app.route("/customers/delete/<id>", methods=["DELETE"])
def delete_customer(id):
    con = sql.connect('msprDev')
    customer_db = CustomerDB(con)
    customer_db.delete_customer(id)
    con.close()
    return f"Customer with id : {id} deleted"


# Product methods
@app.route("/products", methods=["GET"])
def get_products():
    con = sql.connect('msprDev')
    product_db = ProductDB(con)
    rows = product_db.get_all_products() 
    con.close()
    return rows

@app.route("/products/<id>", methods=["GET"])
def get_product_by_id(id):
    con = sql.connect("msprDev")
    product_db = ProductDB(con)
    product_datas = product_db.get_product_by_id(id) 
    con.close()
    return product_datas

@app.route("/products/add", methods=["POST"])
def add_product():
    data = request.data
    json_product = get_bytes_to_json(data)
    
    con = sql.connect('msprDev')
    product_db = ProductDB(con)
    product_db.add_product(json_to_product(json_product))
    con.close()
    return json_product
    
@app.route("/products/update", methods=["PUT"])
def update_product():
    
    data = request.data
    json_product = get_bytes_to_json(data)
    
    con = sql.connect('msprDev')
    product_db = ProductDB(None, con)
    product = json_to_product(json_product)
    product_db.update_product(product)
    con.close()
    return f"Product with id : {product.get_id()} updated"    

@app.route("/products/delete/<id>", methods=["DELETE"])
def delete_product(id):
    con = sql.connect('msprDev')
    product_db = ProductDB(con)
    product_db.delete_product(id)
    con.close()
    return f"Product with id : {id} deleted"

#orders methods
@app.route("/orders", methods=["GET"])
def get_orders():
    con = sql.connect("msprDev")
    order_db = OrderDB(con)
    rows = order_db.get_all_orders()   
    con.close() 
    return rows

@app.route("/customers/<id>/orders", methods=["GET"])
def get_orders_by_customer_id(id):
    con = sql.connect("msprDev")
    order_db = OrderDB(con)
    rows = order_db.get_order_by_id(id)  
    con.close() 
    return rows
    


if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')