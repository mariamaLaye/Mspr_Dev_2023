import json
import sqlite3 as sql

from modele.Customer import json_to_customer

class CustomerDB:
    def __init__(self, datas, con):
        self.datas = datas
        self.con = con
        
        
    def fill_customer(self):
        try:
            c = self.con.cursor() 
            print("here")
            self.con.execute("DELETE FROM Customer")
            for customer in self.datas:
                self.insert_customer(c, json_to_customer(customer))
            self.con.commit()
        except:
            raise sql.DatabaseError("insertion in table Customer failed")
        
    def get_all_customers(self):
        self.con.row_factory = sql.Row

        cursor = self.con.cursor()
        cursor.execute("SELECT * from Customer")

        rows = cursor.fetchall(); 
        return json.dumps([dict(customer) for customer in rows])
       
    def get_customer(self, id):
        try:
            self.con.row_factory = sql.Row
            cursor = self.con.cursor()

            cursor.execute(f'SELECT * FROM Customer where id={id}')

            rows = cursor.fetchall(); 
            print([dict(customer) for customer in rows])
            return json.dumps([dict(customer) for customer in rows])
        except:
            raise sql.DatabaseError("No such ID found in Customer table") 

    def insert_customer(self, customer):
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

    def edit_customer(self, new_customer):
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
        
    def delete_record(self, id):
        cursor = self.con.cursor()
        cursor.execute(f'DELETE FROM Customer WHERE id={id}')  
        self.con.commit()
        
    def close_con(self):
        self.con.close()