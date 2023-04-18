import random as rand


class Product:
    def __init__(self, created_at=str(), customer_id=str(), id=str()):
        self.id = id
        self.created_at = created_at
        self.customer_id = customer_id
        
    def get_id(self):
        return self.id
    
    def get_date(self):
        return self.created_at
    
    def get_customer_id(self):
        return self.customer_id
    
    
    def set_id(self, new_id):
        self.id = new_id
    
    def set_date(self, new_date):
        self.create_at = new_date
        
    def set_customer_id(self, new_customer_id):
        self.customer_id = new_customer_id    
    
    def __repr__(self):
        return f'{self.id}, {self.created_at}, {self.customer_id}'


def json_to_product(product_json):
    res = Product()
    
    try:
        res.set_id(product_json['id'])
        res.set_date(product_json['createdAt'])
        res.set_customer_id(product_json['customerId'])
    except:
        
        random_id = str(rand.randrange(200, 300))
        res.set_id(random_id)
        res.set_date("null")
        res.set_customer_id("null") 
    
    return res       