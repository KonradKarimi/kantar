import unittest
import http.server
import threading
import urllib.request
import json

from sort_service.sort_handler import SortService


class TestSortService(unittest.TestCase):

    def setUp(self):
        self.server = http.server.HTTPServer(('localhost', 1234), SortService)
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.start()

        self.host, self.port = self.server.server_address

    def tearDown(self):
        self.server.shutdown()
        self.server_thread.join()

    def test_sort_numbers(self):
        numbers = [5, 4, 3, 2, 1]
        numbers = '%20'.join([str(n) for n in numbers])
        response = urllib.request.urlopen(f'http://{self.host}:{self.port}/sort?numbers={numbers}')
        data = json.loads(response.read().decode('utf-8'))

        self.assertEqual(data['result'], [1, 2, 3, 4, 5])

    def test_reverse_sort_numbers(self):
        numbers = [5, 4, 3, 2, 1]
        numbers = '%20'.join([str(n) for n in numbers])
        response = urllib.request.urlopen(f'http://{self.host}:{self.port}/reverse?numbers={numbers}')
        data = json.loads(response.read().decode('utf-8'))

        self.assertEqual(data['result'], [1, 2, 3, 4, 5])
