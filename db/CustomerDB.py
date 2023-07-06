import json
import sqlite3 as sql
import random as rand

from models.Customer import Customer

class CustomerDB:
    def __init__(self, data, con):
        self.data = data
        self.con = con
        
        
    def fill_customer(self):
        try:
            cursor = self.con.cursor() 
            self.con.execute("DELETE FROM Customer")
            for customer in self.data:
                self.add_customer(json_to_customer(customer))
            self.con.commit()
        except:
            raise sql.DatabaseError("insertion in table Customer failed")
        
    def get_all_customers(self):
        self.con.row_factory = sql.Row

        cursor = self.con.cursor()
        cursor.execute("SELECT * from Customer")

        rows = cursor.fetchall(); 
        return json.dumps([dict(customer) for customer in rows])
       
    def get_customer_by_id(self, id):
        try:
            self.con.row_factory = sql.Row
            cursor = self.con.cursor()

            cursor.execute(f'SELECT * FROM Customer where id={id}')

            rows = cursor.fetchall(); 
            return json.dumps([dict(customer) for customer in rows])
        except:
            raise sql.DatabaseError("No such ID found in Customer table") 

    def add_customer(self, customer):
        cursor = self.con.cursor()
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
        self.con.commit()

    def update_customer(self, new_customer):
        cursor = self.con.cursor()
        params = (
            new_customer.username,
            new_customer.firstname,
            new_customer.lastname,
            new_customer.city,
            new_customer.postal_code,
            new_customer.street,
            new_customer.id
            )
        cursor.execute(f'UPDATE Customer SET username=?, firstname=?, lastname=?, city=?, postalCode=?, street=?      \
                        WHERE id =?', params)
        self.con.commit()
        
    def delete_customer(self, id):
        cursor = self.con.cursor()
        cursor.execute(f'DELETE FROM Customer WHERE id={id}')  
        self.con.commit()
        

def json_to_customer(customer_json):
    res = Customer()
    try:
        res.set_id(customer_json['id'])
    except:
        random_id = str(rand.randrange(200, 300))
        res.set_id(random_id)
        
    try:
        res.set_username(customer_json['username'])
    except: 
        res.set_username("no username")
        
    try:
        res.set_firstname(customer_json['firstName'])    
    except:
        res.set_firstname("no firstname")
        
    try:
        res.set_lastname(customer_json['lastName'])
    except:
        res.set_lastname("no lastname")
        
  
    if type(customer_json['address']) is str:
        res.set_street(customer_json['address'])
        res.set_city("no city")
        res.set_postal_code("no postal code") 
    elif type(customer_json['address']) is dict:      
        try:
            res.set_city(customer_json['address']['city'])
        except:
            res.set_city("no city") 
        try:       
            res.set_postal_code(customer_json['address']['postalCode']) 
        except:
            res.set_postal_code("no postal code")          
        res.set_street("no street")
    return res        
        
        