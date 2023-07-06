import random as rand


class Product:
    def __init__(
        self, id=str(), product_date=str(), price=str(),
        description=str(), color=str(), stock=str()
        ):
        
        self.id = id
        self.product_date = product_date
        self.price = price
        self.description = description
        self.color = color
        self.stock = stock
        
    def get_id(self):
        return self.id
    
    def get_product_date(self):
        return self.product_date
    
    def get_price(self):
        return self.price

    def get_description(self):
        return self.description
    
    def get_color(self):
        return self.color
    
    def get_stock(self):
        return self.stock
    
    
    def set_id(self, new_id):
        self.id = new_id
    
    def set_product_date(self, new_product_date):
        self.product_date = new_product_date
        
    def set_price(self, new_price):
        self.price = new_price
    
    def set_description(self, new_description):
        self.description = new_description
    
    def set_color(self, new_color):
        self.color = new_color
    
    def set_stock(self, new_stock):
        self.stock = new_stock               
        
    
    def __repr__(self):
        return f'[id={self.id}, date={self.created_at}, CustomerId={self.customer_id}]'


def json__to_product(json_product):
    pass   