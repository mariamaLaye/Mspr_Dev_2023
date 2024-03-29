import unittest
from models.Customer import Customer, json_to_customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer_json = {
            "id": "28",
            "username": "Major89",
            "firstname": "Evalyn",
            "lastname": "Cormier",
            "city": "Port Corene",
            "postalCode": "55015",
            "street": "no street"
        }

    def test_get_id(self):
        customer = json_to_customer(self.customer_json)
        self.assertEqual(customer.get_id(), "28")

    def test_get_username(self):
        customer = json_to_customer(self.customer_json)
        self.assertEqual(customer.get_username(), "Major89")

    def test_get_firstname(self):
        customer = json_to_customer(self.customer_json)
        self.assertEqual(customer.get_firstname(), "Evalyn")

    def test_get_lastname(self):
        customer = json_to_customer(self.customer_json)
        self.assertEqual(customer.get_lastname(), "Cormier")

    def test_get_city(self):
        customer = json_to_customer(self.customer_json)
        self.assertEqual(customer.get_city(), "Port Corene")

    def test_get_postal_code(self):
        customer = json_to_customer(self.customer_json)
        self.assertEqual(customer.get_postal_code(), "55015")

    def test_get_street(self):
        customer = json_to_customer(self.customer_json)
        self.assertEqual(customer.get_street(), "no street")

    def test_set_id(self):
        customer = Customer()
        customer.set_id("2")
        self.assertEqual(customer.get_id(), "2")

    def test_set_username(self):
        customer = Customer()
        customer.set_username("jane_smith")
        self.assertEqual(customer.get_username(), "jane_smith")

    def test_set_firstname(self):
        customer = Customer()
        customer.set_firstname("Jane")
        self.assertEqual(customer.get_firstname(), "Jane")

    def test_set_lastname(self):
        customer = Customer()
        customer.set_lastname("Smith")
        self.assertEqual(customer.get_lastname(), "Smith")

    def test_set_city(self):
        customer = Customer()
        customer.set_city("London")
        self.assertEqual(customer.get_city(), "London")

    def test_set_postal_code(self):
        customer = Customer()
        customer.set_postal_code("67890")
        self.assertEqual(customer.get_postal_code(), "67890")

    def test_set_street(self):
        customer = Customer()
        customer.set_street("123 Main St")
        self.assertEqual(customer.get_street(), "123 Main St")

    def test_json_to_customer(self):
        customer_json = {
            "id" : "250",
            "username": "jane_doe",
            "firstname": "Jane",
            "lastname": "Doe",
            "street": "no street",
            "city": "Los Angeles",
            "postalCode": "54321"
        }
        customer = json_to_customer(customer_json)
        self.assertEqual(customer.get_id(), "250")

if __name__ == '__main__':
    unittest.main()
