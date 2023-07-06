import unittest
from unittest.mock import patch
from models.Product import Product, json_to_product

class TestProduct(unittest.TestCase):

    def setUp(self):
        self.product_json = {
            "id": "1",
            "createdAt": "2023-02-20 04:32:34",
            "customerId": "123"
        }

    def test_get_id(self):
        product = json_to_product(self.product_json)
        self.assertEqual(product.get_id(), "1")

    def test_get_date(self):
        product = json_to_product(self.product_json)
        self.assertEqual(product.get_date(), "2023-02-20 04:32:34")

    def test_get_customer_id(self):
        product = json_to_product(self.product_json)
        self.assertEqual(product.get_customer_id(), "123")

    def test_set_id(self):
        product = Product()
        product.set_id("2")
        self.assertEqual(product.get_id(), "2")

    def test_set_date(self):
        product = Product()
        product.set_date("2023-07-01 10:23:09")
        self.assertEqual(product.get_date(), "2023-07-01 10:23:09")

    def test_set_customer_id(self):
        product = Product()
        product.set_customer_id("456")
        self.assertEqual(product.get_customer_id(), "456")

    def test_json_to_product_with_random_id(self):
        product_json = {
            "id" : "250",
            "createdAt": "null",
            "customerId": "null"
        }
        product = json_to_product(product_json)
        self.assertEqual(product.get_id(), "250")
        self.assertEqual(product.get_date(), "null")
        self.assertEqual(product.get_customer_id(), "null")

if __name__ == '__main__':
    unittest.main()
