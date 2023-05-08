import argparse
import http.server
import logging
import urllib.parse
import json

SORT_SERVER_DEFAULT_PORT = 8080
SORT_SERVER_DEFAULT_HOST = 'localhost'

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)


def get_numbers_from_query(query):
    """
    Extracts the numbers from the query string and returns them as a list of integers.
    :param query: a dictionary of query parameters
    :return: a list of integers
    """
    nums = [int(n) for n in query['numbers'][0].split()]
    return nums


def sort_numbers(nums: list[int]):
    """
    Sorts the given list of numbers and returns the sorted list.
    :param nums: a list of numbers
    :return a sorted list of numbers
    """
    return sorted(nums)


def reverse_sort_numbers(nums):
    """
    Sorts the given list of numbers in reverse order and returns the sorted list.
    :param nums: a list of numbers
    :return: a sorted in reverse order list of numbers
    """
    return list(reversed(nums))


class SortService(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            url_parts = urllib.parse.urlparse(self.path)
            path = url_parts.path
            query = urllib.parse.parse_qs(url_parts.query)

            if path != '/sort' and path != '/reverse':
                logging.error(f'invalid request: {path}')
                self.send_response(404)
                self.end_headers()
                return

            nums = get_numbers_from_query(query)

            if path == '/sort':
                result = sort_numbers(nums)
                logging.info(f'sorted {nums} -> {result}')

            if path == '/reverse':
                result = reverse_sort_numbers(nums)
                logging.info(f'reversed {nums} -> {result}')

            response = json.dumps({'result': result}).encode()
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Content-length', str(len(response)))
            self.end_headers()
            self.wfile.write(response)
        except Exception as e:
            logging.error(e)
            self.send_response(500)
            self.end_headers()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sort Service')
    parser.add_argument('--host', default=SORT_SERVER_DEFAULT_HOST, help='server hostname')
    parser.add_argument('--port', type=int, default=SORT_SERVER_DEFAULT_PORT, help='server port')

    args = parser.parse_args()

    logging.info(f'starting server on {args.host}:{args.port}...')
    httpd = http.server.HTTPServer((args.host, args.port), SortService)
    httpd.serve_forever()