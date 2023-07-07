import json
import sqlite3 as sql

from models.Product import Product

class ProductDB():
    
    def __init__(self, con):
        self.con = con
    
     
    def get_all_products(self):
        self.con.row_factory = sql.Row

        cursor = self.con.cursor()
        cursor.execute("SELECT * from Product")

        rows = cursor.fetchall(); 
        return json.dumps([dict(product) for product in rows])
    
    def get_product_by_id(self, id):
        try:
            self.con.row_factory = sql.Row
            cursor = self.con.cursor()

            cursor.execute(f'SELECT * FROM Product where id={id}')

            rows = cursor.fetchall(); 
            return json.dumps([dict(product) for product in rows])
        except:
            raise sql.DatabaseError("No such ID found in Product table") 
    
    def update_product(self, product):
        cursor = self.con.cursor()
        params = (
            product.product_date,
            product.price,
            product.description,
            product.color,
            product.stock,
            product.id
            )
        cursor.execute(f'UPDATE Product SET productDate=?, price=?, description=?, color=?, stock=?\
                        WHERE id =?', params)
        self.con.commit()
    
    def add_product(self, product):
        cursor = self.con.cursor()
        params = (
            product.id,
            product.product_date,
            product.price,
            product.description,
            product.color,
            product.stock
            )
        cursor.execute(f'INSERT INTO Product VALUES (?, DATE(?), ?, ?, ?, ?)', params)
        self.con.commit()
    
    def delete_product(self, id):
        cursor = self.con.cursor()
        cursor.execute(f'DELETE FROM Product WHERE id={id}')  
        self.con.commit()

def json_to_product(json_product, raw=False):
    if raw:
        return Product(
            json_product['id'],
            json_product['createdAt'],
            json_product['details']['price'],
            json_product['details']['description'],
            json_product['details']['color'],
            json_product['stock']
        )
    else:
        return Product(
            json_product['id'],
            json_product['productDate'],
            json_product['price'],
            json_product['description'],
            json_product['color'],
            json_product['stock']
        )
            