import http.client
import sys
from urllib.parse import quote

SERVER_DEFAULT_PORT = 8080
SERVER_DEFAULT_HOST = 'localhost'

if len(sys.argv) < 3:
    print('Usage: client.py {sort|reverse} [int0 int1 ... intn]')
    print('Example: client.py sort 1 2 3 4 5')
    sys.exit()

command = sys.argv[1]
nums = ' '.join(sys.argv[2:])

path = f'/{command}?numbers={quote(nums)}'

conn = http.client.HTTPConnection(SERVER_DEFAULT_HOST, SERVER_DEFAULT_PORT)

conn.request('GET', path)

resp = conn.getresponse()

if resp.status != 200:
    print(f'Error: {resp.status} {resp.reason}')
    sys.exit()

result = resp.read().decode()

print(f'Result: {result}')
