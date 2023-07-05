import random as rand


class Product:
    def __init__(self, id=str(), created_at=str(), customer_id=str()):
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
        self.created_at = new_date
        
    def set_customer_id(self, new_customer_id):
        self.customer_id = new_customer_id    
    
    def __repr__(self):
        return f'[id={self.id}, date={self.created_at}, CustomerId={self.customer_id}]'


def json_to_product(product_json):
    return Product(
        product_json['id'],
        product_json['createdAt'],
        product_json['customerId']
    )       