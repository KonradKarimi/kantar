import argparse
import http.server
import logging

from sort_service.sort_handler import SortHandler

SORT_SERVER_DEFAULT_PORT = 8080
SORT_SERVER_DEFAULT_HOST = 'localhost'


def main():
    parser = argparse.ArgumentParser(description='Sort Service')
    parser.add_argument('--host', default=SORT_SERVER_DEFAULT_HOST, help='server hostname')
    parser.add_argument('--port', type=int, default=SORT_SERVER_DEFAULT_PORT, help='server port')

    args = parser.parse_args()

    logging.info(f'starting server on {args.host}:{args.port}...')
    httpd = http.server.HTTPServer((args.host, args.port), SortHandler)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        logging.info('stopping server...')


if __name__ == '__main__':
    main()
