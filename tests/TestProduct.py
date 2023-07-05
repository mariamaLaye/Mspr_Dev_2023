import unittest
from unittest.mock import patch
from product import Product, json_to_product

class TestProduct(unittest.TestCase):

    def setUp(self):
        self.product_json = {
            "id": "1",
            "createdAt": "2023-06-30",
            "customerId": "123"
        }

    def test_get_id(self):
        product = json_to_product(self.product_json)
        self.assertEqual(product.get_id(), "1")

    def test_get_date(self):
        product = json_to_product(self.product_json)
        self.assertEqual(product.get_date(), "2023-06-30")

    def test_get_customer_id(self):
        product = json_to_product(self.product_json)
        self.assertEqual(product.get_customer_id(), "123")

    def test_set_id(self):
        product = Product()
        product.set_id("2")
        self.assertEqual(product.get_id(), "2")

    def test_set_date(self):
        product = Product()
        product.set_date("2023-07-01")
        self.assertEqual(product.get_date(), "2023-07-01")

    def test_set_customer_id(self):
        product = Product()
        product.set_customer_id("456")
        self.assertEqual(product.get_customer_id(), "456")

    @patch('random.randrange')
    def test_json_to_product_with_random_id(self, mock_randrange):
        mock_randrange.return_value = 250
        product_json = {
            "createdAt": "2023-07-02",
            "customerId": "789"
        }
        product = json_to_product(product_json)
        self.assertEqual(product.get_id(), "250")
        self.assertEqual(product.get_date(), "null")
        self.assertEqual(product.get_customer_id(), "null")

if __name__ == '__main__':
    unittest.main()
