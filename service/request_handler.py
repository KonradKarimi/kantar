import json

from service.response import Response
from service.sort_service import sort_numbers, reverse_sort_numbers


def handle_request(method: str, path: str, **kwargs) -> Response:
    """
    This is the entry point for request handling. Only GET and POST methods are allowed.
    :param method: string containing the request method
    :param path: string containing the request path
    :param kwargs: dictionary containing the request query or body
    :return: Response object
    """

    if path != '/sort' and path != '/reverse':
        return Response(status_code=404, body={'Error': 'Resource Not Found'})
    if method == 'GET':
        return handle_get_method(path, kwargs['query'])
    if method == 'POST':
        return handle_post_method(path, kwargs['body'])

    # Any other methods like DELETE, PUT, etc. are not allowed for this service
    return Response(status_code=405, body={'Error': 'Method Not Allowed'})


def handle_get_method(path: str, query: bytes) -> Response:
    """
    Handles GET requests and returns the response
    :param path: string containing the request path
    :param query: bytes containing the request query
    :return: Response object
    """

    if not query:
        return Response(status_code=400, body={'Error': 'Not provided any numbers to sort'})
    try:
        numbers_to_sort = parse_query_string(query.decode())
    except ValueError:
        return Response(status_code=400, body={'Error': 'Only list of integers is allowed'})
    sorted_numbers = do_sorting(numbers_to_sort, path)
    return Response(status_code=200, body=sorted_numbers)


def handle_post_method(path: str, body: bytes) -> Response:
    """
    Handles POST requests and returns the response
    :param path: string containing the request path
    :param body: bytes containing the request body
    :return:
    """

    if not body:
        return Response(status_code=400, body={'Error': 'Not provided any numbers to sort'})
    if body == b'[]':
        return Response(status_code=400, body={'Error': 'Not provided any numbers to sort - empty list'})
    try:
        numbers_to_sort = parse_request_body(body)
    except ValueError:
        return Response(status_code=400, body={'Error': 'Only list of integers is allowed'})
    sorted_numbers = do_sorting(numbers_to_sort, path)
    return Response(status_code=200, body=sorted_numbers)


def parse_query_string(query: str) -> list[int]:
    """
    Parses the query string and returns a list of integers. The query string is expected to be a string of numbers
    separated by spaces. %20 is used as a separator instead of spaces. For example, the query string '1 2 3' is expected
    to be '1%202%203'.
    :param query: a string containing numbers separated by spaces
    :return: a list of integers
    """
    return [int(n) for n in query.split("%20")]


def do_sorting(numbers_to_sort: list[int], path: str) -> list[int]:
    """
    Sorts the numbers based on the path.
    :param numbers_to_sort: numbers to sort
    :param path: path to select the sorting method from (e.g. /sort or /reverse)
    :return:
    """
    sorted_numbers = None
    if path == '/sort':
        sorted_numbers = sort_numbers(numbers_to_sort)
    elif path == '/reverse':
        sorted_numbers = reverse_sort_numbers(numbers_to_sort)
    return sorted_numbers


def parse_request_body(body: bytes) -> list[int]:
    """
    Parses the request body and returns a list of integers
    :param body: bytes containing the request body
    :return: a list of integers
    """
    body = body.decode("utf-8")
    numbers = [int(n) for n in json.loads(body)]
    return numbers
