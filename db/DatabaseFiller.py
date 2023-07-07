import requests
import sqlite3 as sql
import random as rand

    
class DatabaseFiller:
    
    def __init__(self, con):
        self.con = con
    
    
    def fill_customer(self, data):
        try:
            cursor = self.con.cursor() 
            cursor.execute("DELETE FROM Customer")
            for customer in data:
                res = []  
                try:
                    res.append(customer['id'])
                except:
                    random_id = str(rand.randrange(200, 300))
                    res.append(random_id)
                    
                try:
                    res.append(customer['username'])
                except: 
                    res.append("no username")
                    
                try:
                    res.append(customer['firstName'])    
                except:
                    res.append("no firstname")
                    
                try:
                    res.append(customer['lastName'])
                except:
                    res.append("no lastname")
            
                if type(customer['address']) is str:
                    res.append(customer['address'])
                    res.append("no city")
                    res.append("no postal code") 
                elif type(customer['address']) is dict:      
                    try:
                        res.append(customer['address']['city'])
                    except:
                        res.append("no city") 
                    try:       
                        res.append(customer['address']['postalCode']) 
                    except:
                        res.append("no postal code")          
                    res.append("no street")
                params = (
                    res[0],
                    res[1],
                    res[2],
                    res[3],
                    res[4],
                    res[5],
                    res[6]
                    )
                cursor.execute(f'INSERT INTO Customer VALUES (?, ?, ?, ?, ?, ?, ?)', params)
            self.con.commit()
        except:
            raise sql.DatabaseError("insertion in table Customer failed")  
    
    def fill_product(self, data):
        try:    
            cursor = self.con.cursor()
            cursor.execute("DELETE FROM Product")
            for i in range(len(data)):
                params = (
                    data[i]['id'],
                    data[i]['createdAt'],
                    data[i]['details']['price'],
                    data[i]['details']['description'],
                    data[i]['details']['color'],
                    data[i]['stock']
                    )
                cursor.execute(f'INSERT INTO Product VALUES (?, DATE(?), ?, ?, ?, ?)', params)
        except:
            raise sql.DatabaseError("insertion in table failed")
        self.con.commit()

    def fill_order(self, data):
        try:    
            cursor = self.con.cursor()
            cursor.execute('DELETE FROM "Order"')
            for i in range(len(data)):
                if len(data[i]['orders']) > 0:
                    for json_order in data[i]['orders']:
                        params = (
                            json_order['id'],
                            json_order['createdAt'],
                            json_order['customerId']
                        )
                        cursor.execute(f'INSERT INTO "Order" VALUES (?, DATETIME(?), ?)', params)
        except:
            raise sql.DatabaseError("insertion in table failed")
        self.con.commit()  

    
def get_all_data(data_type):
    response = requests \
        .get(f"https://615f5fb4f7254d0017068109.mockapi.io/api/v1/{data_type}/")
    data = response.json()
    return data     
    
#refile all database
con = sql.connect('../msprDev')
customer_data = get_all_data("customers")
product_data  = get_all_data("products")

db_filler = DatabaseFiller(con)

db_filler.fill_customer(customer_data)
db_filler.fill_product(product_data)
db_filler.fill_order(customer_data)

con.close()
