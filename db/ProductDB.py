import json
import sqlite3 as sql
import random as rand

from modele.Product import Product, json_to_product 

class ProductDB:
    
    def __init__(self, datas, con):
        self.datas = datas        
        self.con = con
        
        
    def fill_product(self):
        try:    
            cursor = self.con.cursor()
            cursor.execute("DELETE FROM Product")
            for i in range(len(self.datas)):
                if len(self.datas[i]['orders']) > 0:
                    for product in self.datas[i]['orders']:
                        self.add_product(json_to_product(product))
        except:
            raise sql.DatabaseError("insertion in table failed")
        self.con.commit()

    def get_all_products(self):
        self.con.row_factory = sql.Row

        cursor = self.con.cursor()
        cursor.execute("SELECT * from Product")

        rows = cursor.fetchall(); 
        return json.dumps([dict(product) for product in rows])

    def get_product(self, id):
        try:
            self.con.row_factory = sql.Row
            cursor = self.con.cursor()

            cursor.execute(f'SELECT * FROM Product where id={id}')
            rows = cursor.fetchall(); 
            return json.dumps([dict(products) for products in rows])
        except:
            raise sql.DatabaseError("No such ID found in Product table") 


    def update_product(self, product):
        cursor = self.con.cursor()
        print(f'UPDATE Product SET createdAt={product.get_date()} WHERE id={product.get_id()}')
        cursor.execute(f'UPDATE Product SET createdAt="{product.get_date()}" WHERE id={product.get_id()}')
        self.con.commit()
        
        
    def add_product(self, product):
        print(product)
        params = (
            product.id,
            product.created_at,
            product.customer_id
        )
        print(params)
        cursor = self.con.cursor()
        try:
            cursor.execute(f'SELECT * FROM Customer WHERE id={product.customer_id}')
            cursor.execute(f'INSERT INTO Product VALUES (?, DATETIME(?), ?)', params)
            self.con.commit()   
        except:
            raise sql.DatabaseError("You must add a product with an existing customerID") 
        
    
    def delete_product(self, id):
        cursor = self.con.cursor()
        cursor.execute(f'DELETE FROM Product WHERE id={id}')    
        self.con.commit()
        
def json_to_product(json_product):
    product_json = Product()
    try:
        product_json.set_id(json_product['id'])
        product_json.set_date(json_product['createdAt'])
        product_json.set_customer_id(json_product['customerId'])
    except:
        random_id = str(rand.randrange(100, 300) + rand.randrange(1, 10))
        product_json.set_id(random_id)
        product_json.set_date("null")
        product_json.set_customer_id("null")     
    return product_json       