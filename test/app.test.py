import unittest
from unittest import mock
from api.main import app, URL_PREFIX

def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == 'http://someurl.com/test.json':
        return MockResponse({"key1": "value1"}, 200)
    elif args[0] == 'http://someotherurl.com/anothertest.json':
        return MockResponse({"key2": "value2"}, 200)

    return MockResponse(None, 404)

class AppTest(unittest.TestCase):
    client = app.test_client()

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_items(self):
        response = self.client.get('{}/'.format(URL_PREFIX))
        assert response.content_length == 0
