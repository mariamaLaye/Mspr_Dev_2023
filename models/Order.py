class Order:
    
    def __init__(self, customer_id=str(), order_date=str(), product_id=str()):
        self.customer_id = customer_id
        self.order_date = order_date
        self.product_id = product_id
        
        
    def get_customer_id(self):
        return self.customer_id
    
    def get_order_date(self):
        return self.order_date
    
    def get_product_id(self):
        return self.product_id 
    
    
    def set_customer_id(self, new_customer_id):
        self.customer_id = new_customer_id
        
    def set_order_date(self, new_order_date):
        self.order_date = new_order_date
        
    def set_product_id(self, new_product_id):
        self.product_id = new_product_id
        
        
    def __repr__(self):
        return f'[CustomerID={self.customer_id} OrderDate={self.order_date} ProductID={self.product_id}]'    
         
def json_to_order(order_json):
    return Order(
        order_json['id'],
        order_json['createdAt'],
        order_json['customerId']
    )          