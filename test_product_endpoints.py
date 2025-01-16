import unittest
from unittest.mock import patch, MagicMock
from app import app

class TestProductEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('controllers.productController.create_product')
    def test_create_product(self, mock_create_product):
        mock_create_product.return_value = ('{"message": "Product created successfully"}', 201)
        response = self.app.post('/products', json={'name': 'Test Product', 'price': 10.99})
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Product created successfully', response.data)

    @patch('controllers.productController.get_product')
    def test_get_product(self, mock_get_product):
        mock_get_product.return_value = ('{"message": "Product retrieved successfully", "data": {"id": 1, "name": "Test Product", "price": 10.99}}', 200)
        response = self.app.get('/products/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Product retrieved successfully', response.data)

    @patch('controllers.productController.update_product')
    def test_update_product(self, mock_update_product):
        mock_update_product.return_value = ('{"message": "Product updated successfully"}', 200)
        response = self.app.put('/products/1', json={'name': 'Updated Product', 'price': 12.99})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Product updated successfully', response.data)

    @patch('controllers.productController.delete_product')
    def test_delete_product(self, mock_delete_product):
        mock_delete_product.return_value = ('{"message": "Product deleted successfully"}', 200)
        response = self.app.delete('/products/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Product deleted successfully', response.data)

if __name__ == '__main__':
    unittest.main()