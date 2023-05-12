import http.client
import logging
import os
import pprint
import sys
import argparse

DEFAULT_HOST = 'localhost'
DEFAULT_PORT = 8000


class Request:
    """
    Represents an HTTP request.
    """

    def __init__(self, method: str, path: str, query: str, body: bytes):
        """
        Initializes a new instance of the Request class.
        :param method: the HTTP method
        :param path: the HTTP path
        :param query: the HTTP query string
        :param body: the HTTP body
        """
        self.method = method
        self.path = path
        self.query = query
        self.body = body

    def send_request(self):
        """
        Sends an HTTP request.
        :return: None
        """
        try:
            conn = http.client.HTTPConnection(DEFAULT_HOST, DEFAULT_PORT)
            url = self.path + '?' + self.query
            conn.request(self.method, url)
            response = conn.getresponse()
            handle_response(response)
        except Exception as e:
            logging.error(e)
            sys.exit(1)


def handle_response(response):
    """
    Handles an HTTP response.
    :param response: the HTTP response
    :return:
    """
    if response.status != 200:
        logging.error(f'error: {response.status} {response.reason}')
        sys.exit(1)

    print(f"response: {response.read().decode('utf-8')}")


def prepare_query_string(numbers: list[int]) -> str:
    """
    Prepares the query string from the given numbers. The query string is a space-separated list of numbers. The
    space is encoded as %20.
    :param numbers: a list of numbers
    :return: a query string
    """
    return '%20'.join([str(n) for n in numbers])


def sort(numbers: list[int]):
    """
    Sorts the given numbers.
    :param numbers: a list of numbers
    :return: None
    """
    query_string = prepare_query_string(numbers)
    Request('GET', '/sort', query_string, b'').send_request()


def reverse(numbers: list[int]):
    """
    Sorts the given numbers in reverse order.
    :param numbers: a list of numbers
    :return: None
    """
    query_string = prepare_query_string(numbers)
    Request('GET', '/reverse', query_string, b'').send_request()


def main():
    """
    Main entry point for the client application.
    """
    parser = argparse.ArgumentParser(description='Sort Client')
    parser.add_argument('command', type=str, help='the command to execute (sort or reverse)')
    parser.add_argument('numbers', type=int, nargs='+', help='the numbers to sort')
    args = parser.parse_args()

    if args.command == 'sort':
        sort(args.numbers)
    elif args.command == 'reverse':
        reverse(args.numbers)
    else:
        print(f'invalid command: {args.command}')
        sys.exit(1)


if __name__ == '__main__':
    main()
