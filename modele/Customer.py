import random as rand

class Customer:
    
    def __init__(
        self, id=str(), username=str(), firstname=str(),
        lastname=str(), city=str(), postal_code=str(), street=str()):
        
        self.id = id
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.city = city
        self.postal_code = postal_code
        self.street = street

    
    def get_id(self):
        return self.id   
     
    def get_username(self):
        return self.username   
    
    def get_firstname(self):
        return self.firstname                

    def get_lastname(self):
        return self.lastname      
    
    def get_city(self):
        return self.city
       
    def get_postal_code(self):
        return self.postal_code 
    
    def get_street(self):
        return self.street
    
    
    def set_id(self, new_id):
        self.id = new_id
     
    def set_username(self, new_username):
        self.username = new_username   
    
    def set_lastname(self, new_lastname):
        self.lastname = new_lastname                 

    def set_firstname(self, new_firstname):
        self.firstname = new_firstname      
    
    def set_city(self, new_city):
        self.city = new_city
       
    def set_postal_code(self, new_postal_code):
        self.postal_code = new_postal_code
        
    def set_street(self, new_street):
        self.street = new_street    
    
    def __repr__(self):
        return f'[id={self.id}, username={self.username}, firstname={self.firstname}, \
            lastname={self.lastname}, city={self.city}, postal code={self.postal_code}, street={self.street}]'
            
                  
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