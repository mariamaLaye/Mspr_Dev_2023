import json
import sqlite3 as sql
import random as rand

from models.Order import Order, json_to_order 

class OrderDB:
    
    def __init__(self, con):
        self.con = con

    def get_all_orders(self):
        self.con.row_factory = sql.Row

        cursor = self.con.cursor()
        cursor.execute('SELECT * from "Order"')

        rows = cursor.fetchall(); 
        return json.dumps([dict(order) for order in rows])

    def get_order_by_id(self, id):
        try:
            self.con.row_factory = sql.Row
            cursor = self.con.cursor()

            cursor.execute(f'SELECT * FROM "Order" where customerId={id}')
            rows = cursor.fetchall(); 
            return json.dumps([dict(order) for order in rows])
        except:
            raise sql.DatabaseError("No such ID found in Order table") 


    def update_order(self, order):
        cursor = self.con.cursor()
        cursor.execute(f'UPDATE "Order" SET createdAt="{order.get_date()}" \
            WHERE customerId={order.customer_id} AND product_id={order.product_id}')
        self.con.commit()
        

    def add_order(self, order):
        params = (
            order.id,
            order.created_at,
            order.customer_id
        )
        cursor = self.con.cursor()
        try:
            cursor.execute(f'SELECT * FROM Customer WHERE id={order.customer_id}')
            cursor.execute(f'SELECT * FROM Product WHERE id={order.product_id}')
            cursor.execute(f'INSERT INTO "Order" VALUES (?, DATETIME(?), ?)', params)
            self.con.commit()   
        except:
            raise sql.DatabaseError("You must add an order with an existing customerID and productID") 
        
    
    def delete_order(self, customer_id, product_id):
        cursor = self.con.cursor()
        cursor.execute(f'DELETE FROM "Order" WHERE customer_id={customer_id} AND product_id={product_id}')    
        self.con.commit()
        
def json_to_order(json_order):
    return Order(
        json_order['id'],
        json_order['createdAt'],
        json_order['customerId']
    )    