from multiprocessing import Process
import asynctest
import asyncio
import uvicorn
import requests


class TestServerConnection(asynctest.TestCase):
    """Test the connection to the server and other basic functionality"""

    async def setUp(self):
        self.process = Process(target=uvicorn.run, args=("main:app",),
                               kwargs=dict(port=8000, log_level="trace", host="localhost"),
                               daemon=True)
        self.process.start()
        await asyncio.sleep(1)

    async def tearDown(self):
        self.process.terminate()
        await asyncio.sleep(1)

    async def test_connect(self):
        """connect to the server and get a response"""
        response = requests.get("http://localhost:8000/sort?1%202%203")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [1, 2, 3])

    async def test_invalid_path(self):
        """connect to the server and request an invalid resource"""
        response = requests.get("http://localhost:8000/invalid_path")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {'Error': 'Resource Not Found'})

    async def test_unavailable_method(self):
        """connect to the server and request a resource with an unavailable method"""
        response = requests.delete("http://localhost:8000/sort?1%202%203")
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.json(), {'Error': 'Method Not Allowed'})

    async def test_invalid_query(self):
        """connect to the server and request a resource with an invalid query containing letter 'a'"""
        response = requests.get("http://localhost:8000/sort?1%202%20a")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'Error': 'Only list of integers is allowed'})

    async def test_empty_query(self):
        """connect to the server and request a resource with an empty query"""
        response = requests.get("http://localhost:8000/sort?")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'Error': 'Not provided any numbers to sort'})

    async def test_empty_body(self):
        """connect to the server and request a resource with an empty body"""
        response = requests.post("http://localhost:8000/sort", data="")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'Error': 'Not provided any numbers to sort'})

    async def test_float_numbers(self):
        """connect to the server and request a resource with float numbers"""
        response = requests.post("http://localhost:8000/sort", data="[1.1 2.2 3.3]")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'Error': 'Only list of integers is allowed'})
