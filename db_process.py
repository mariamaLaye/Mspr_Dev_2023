import sqlite3 as sql
import secrets
from app import get_all_datas
from modele.Customer import json_to_customer
from modele.Product import json_to_product


def insert_customer(datas=get_all_datas()):
    try:
        con = sql.connect('msprDev')
        c = con.cursor() 
        con.execute("DELETE FROM Customer")
        for elem in datas:
            insert_single_customer(c, elem)
        con.commit()
    except:
        raise sql.DatabaseError("connection to database or insertion in table failed")
    
def insert_product(datas=get_all_datas()):
    try:
        con = sql.connect('msprDev')    
        c = con.cursor()
        con.execute("DELETE FROM Product")
        for i in range(len(datas)):
            print(datas[i])
            if len(datas[i]['orders']) > 0:
                for product in datas[i]['orders']:
                    insert_single_product(c, product)
        con.commit()
    except:
        raise sql.DatabaseError("connection to database or insertion in table failed")

# def insert_user():
#     try:
#         con = sql.connect('msprDev')
#         c = con.cursor()
#         auth_key = secrets.token_urlsafe(16)

            
def insert_single_customer(cursor, data):
    customer = json_to_customer(data)
    params = (
        customer.id,
        customer.username,
        customer.firstname,
        customer.lastname,
        customer.city,
        customer.postal_code,
        customer.street
        )
    cursor.execute(f'INSERT INTO Customer VALUES (?, ?, ?, ?, ?, ?, ?)', params)
 
def insert_single_product(cursor, data):
    product = json_to_product(data) 
    params = (
        product.id,
        product.create_at,
        product.customer_id
    )
    cursor.execute(f'INSERT INTO Product VALUES (?, DATETIME(?), ?)', params)
    
    
     