import unittest
from unittest.mock import patch, MagicMock
from app import app
from models.order import Order

class TestOrderEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('controllers.orderController.create_order')
    def test_create_order(self, mock_create_order):
        mock_create_order.return_value = ('{"message": "Order created successfully"}', 201)
        response = self.app.post('/orders', json={
            'customer_id': 1,
            'product_id': 1,
            'order_date': '2023-10-10T00:00:00',
            'quantity': 2
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Order created successfully', response.data)

    @patch('controllers.orderController.get_order')
    def test_get_order(self, mock_get_order):
        mock_get_order.return_value = ('{"message": "Order retrieved successfully"}', 200)
        response = self.app.get('/orders/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Order retrieved successfully', response.data)

    @patch('controllers.orderController.update_order')
    def test_update_order(self, mock_update_order):
        mock_update_order.return_value = ('{"message": "Order updated successfully"}', 200)
        response = self.app.put('/orders/1', json={
            'quantity': 3
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Order updated successfully', response.data)

    @patch('controllers.orderController.delete_order')
    def test_delete_order(self, mock_delete_order):
        mock_delete_order.return_value = ('{"message": "Order deleted successfully"}', 200)
        response = self.app.delete('/orders/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Order deleted successfully', response.data)

if __name__ == '__main__':
    unittest.main()