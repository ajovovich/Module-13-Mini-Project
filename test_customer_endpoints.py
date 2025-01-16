import unittest
from unittest.mock import patch, MagicMock
from app import app
from models.customer import Customer

class TestCustomerEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('models.customer.Customer.query.get_or_404')
    def test_get_customer(self, mock_get):
        mock_customer = MagicMock(spec=Customer)
        mock_customer.to_dict.return_value = {'id': 1, 'name': 'John Doe', 'email': 'john@example.com'}
        mock_get.return_value = mock_customer

        response = self.app.get('/customer/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Customer retrieved successfully', response.json['message'])
        self.assertEqual(response.json['data'], {'id': 1, 'name': 'John Doe', 'email': 'john@example.com'})

    @patch('models.customer.Customer.query.get_or_404')
    @patch('app.db.session.commit')
    @patch('app.db.session.rollback')
    def test_update_customer(self, mock_rollback, mock_commit, mock_get):
        mock_customer = MagicMock(spec=Customer)
        mock_customer.to_dict.return_value = {'id': 1, 'name': 'John Doe', 'email': 'john@example.com'}
        mock_get.return_value = mock_customer

        response = self.app.put('/customer/1', json={'name': 'Jane Doe', 'email': 'jane@example.com'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Customer updated successfully', response.json['message'])
        self.assertEqual(response.json['data'], {'id': 1, 'name': 'John Doe', 'email': 'john@example.com'})

    @patch('models.customer.Customer.query.get_or_404')
    @patch('app.db.session.commit')
    @patch('app.db.session.rollback')
    def test_delete_customer(self, mock_rollback, mock_commit, mock_get):
        mock_customer = MagicMock(spec=Customer)
        mock_get.return_value = mock_customer

        response = self.app.delete('/customer/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Customer deleted successfully', response.json['message'])

    @patch('models.customer.Customer.query.all')
    def test_get_customers(self, mock_all):
        mock_customer1 = MagicMock(spec=Customer)
        mock_customer1.to_dict.return_value = {'id': 1, 'name': 'John Doe', 'email': 'john@example.com'}
        mock_customer2 = MagicMock(spec=Customer)
        mock_customer2.to_dict.return_value = {'id': 2, 'name': 'Jane Doe', 'email': 'jane@example.com'}
        mock_all.return_value = [mock_customer1, mock_customer2]

        response = self.app.get('/customers')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Customers retrieved successfully', response.json['message'])
        self.assertEqual(response.json['data'], [
            {'id': 1, 'name': 'John Doe', 'email': 'john@example.com'},
            {'id': 2, 'name': 'Jane Doe', 'email': 'jane@example.com'}
        ])

if __name__ == '__main__':
    unittest.main()