import asyncio
import uvicorn

from service.request_handler import handle_request


async def read_body(receive):
    """
    Read and return the entire body from an incoming ASGI message.
    """
    body = b''
    more_body = True

    while more_body:
        message = await receive()
        body += message.get('body', b'')
        more_body = message.get('more_body', False)

    return body


async def app(scope, receive, send):
    """
    This is the entry point for the ASGI server.
    :param scope: dictionary containing information about the connection
    :param receive: channel for receiving messages
    :param send: channel for sending messages
    :return: None
    """
    assert scope['type'] == 'http'
    request_method = scope['method']
    request_path = scope['path']
    query_string = scope['query_string']
    body = await read_body(receive)

    # Handle the request (see sort_service/request_handler.py)
    await handle_request(request_method, request_path, query=query_string, body=body).send_response(send)


async def main():
    config = uvicorn.Config(app="main:app", port=8000, log_level="trace")
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == '__main__':
    asyncio.run(main())
