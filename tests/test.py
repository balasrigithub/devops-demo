import unittest
from main.app import create_app

class CleanerTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.testing = True

    def test_valid_input(self):
        with self.app.test_client() as client:
            response = client.post('/', json={'document':'this is a test'})
            self.assertEqual(response.status_code, 200)
            self.assertIn('tokens', response.get_json(), 'invalid json returned')