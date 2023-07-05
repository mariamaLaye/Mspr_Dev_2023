import json
import sqlite3 as sql

from modele.Product import json_to_product 

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
                        self.insert_product(json_to_product(product))
            self.con.commit()
        except:
            raise sql.DatabaseError("insertion in table failed")

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

            rows = self.cursor.fetchall(); 
            return json.dumps([dict(products) for products in rows])
        except:
            raise sql.DatabaseError("No such ID found in Product table") 


    def edit_product(self, new_date, id_product):
        cursor = self.con.cursor()
        cursor.execute(f'UPDATE Product SET createdAt={new_date} WHERE id={id_product}')
        self.con.commit()
        
        
    def insert_product(self, product):
        params = (
            product.id,
            product.created_at,
            product.customer_id
        )
        self.cursor.execute(f'INSERT INTO Product VALUES (?, DATETIME(?), ?)', params)
        self.con.commit()   
        
    
    def delete_record(self, id):
        cursor = self.con.cursor()
        cursor.execute(f'DELETE FROM Product WHERE id={id}')    
        self.con.commit()