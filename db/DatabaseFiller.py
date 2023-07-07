import requests
import sqlite3 as sql

from db.CustomerDB import CustomerDB, json_to_customer
from db.OrderDB import OrderDB
from db.ProductDB import ProductDB, json_to_product
from models.Order import json_to_order
    
class DatabaseFiller:
    
    def __init__(self, con):
        self.con = con
   
    
    def fill_customer(self, data):
        customer_db = CustomerDB(self.con)
        try:
            cursor = self.con.cursor() 
            cursor.execute("DELETE FROM Customer")
            for customer in data:
                customer_db.add_customer(json_to_customer(customer))
            self.con.commit()
        except:
            raise sql.DatabaseError("insertion in table Customer failed")  
    
    def fill_product(self, data):
        product_db = ProductDB(self.con)
        try:    
            cursor = self.con.cursor()
            cursor.execute("DELETE FROM Product")
            for i in range(len(data)):
                product_db.add_product(json_to_product(data[i]))
        except:
            raise sql.DatabaseError("insertion in table failed")
        self.con.commit()

    def fill_order(self, data):
        order_db = OrderDB(self.con)
        try:    
            cursor = self.con.cursor()
            cursor.execute('DELETE FROM "Order"')
            for i in range(len(data)):
                if len(data[i]['orders']) > 0:
                    for order in data[i]['orders']:
                        order_db.add_order(json_to_order(order))
        except:
            raise sql.DatabaseError("insertion in table failed")
        self.con.commit()  

    
def get_all_data(data_type):
    response = requests \
        .get(f"https://615f5fb4f7254d0017068109.mockapi.io/api/v1/{data_type}/")
    data = response.json()
    return data     
    
#refile all database
con = sql.connect('msprDev')
customer_data = get_all_data("customers")
product_data  = get_all_data("products")

db_filler = DatabaseFiller(con)

db_filler.fill_customer(customer_data)
db_filler.fill_product(product_data)
db_filler.fill_order(customer_data)
