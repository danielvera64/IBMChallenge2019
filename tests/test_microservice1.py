import json
from unittest import TestCase
from api import app


class TestMicroservice1(TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        data = {
            "elements": [25, 4, "", "Banana", "Orange", "Apple", "Mango", 1.23, 4.5, None]
        }
        self.response_10 = self.client.post(path='/ibmchallengemic1/element_sorter1_0',
                                            data=json.dumps(data),
                                            content_type='application/json')

        self.json_data_10 = self.response_10.get_json(force=True)

        self.response_11 = self.client.post(path='/ibmchallengemic1/element_sorter1_1',
                                            data=json.dumps(data),
                                            content_type='application/json')

        self.json_data_11 = self.response_11.get_json(force=True)

    def test_status_code(self):
        self.assertEqual(self.response_10.status_code, 200)
        self.assertEqual(self.response_11.status_code, 200)

    def test_response_10_type(self):
        self.assertIn('data', self.json_data_10)
        self.assertIn('sorted', self.json_data_10['data'])
        self.assertIsInstance(self.json_data_10['data']['sorted'], list)

    def test_10_sorting(self):
        self.assertIs(len(self.json_data_10['data']['sorted']), 8)

        self.assertIsInstance(self.json_data_10['data']['sorted'][0], str)

        self.assertEqual(self.json_data_10['data']['sorted'][0], "1.23")
        self.assertEqual(self.json_data_10['data']['sorted'][7], "Orange")

    def test_response_11_type(self):
        self.assertIn('data', self.json_data_11)

        self.assertIn('numbers', self.json_data_11['data'])
        self.assertIsInstance(self.json_data_11['data']['numbers'], list)

        self.assertIn('others', self.json_data_11['data'])
        self.assertIsInstance(self.json_data_11['data']['others'], list)

    def test_11_sorting(self):
        self.assertIs(len(self.json_data_11['data']['numbers']), 4)
        self.assertIsInstance(self.json_data_11['data']['numbers'][0], float)
        self.assertEqual(self.json_data_11['data']['numbers'][0], 1.23)
        self.assertEqual(self.json_data_11['data']['numbers'][3], 25)

        self.assertIs(len(self.json_data_11['data']['others']), 4)
        self.assertIsInstance(self.json_data_11['data']['others'][0], str)
        self.assertEqual(self.json_data_11['data']['others'][0], "Apple")
        self.assertEqual(self.json_data_11['data']['others'][3], "Orange")
