import json
from dataclasses import dataclass


@dataclass
class Response:
    """
    Response dataclass for sending responses to the client.
    """
    status_code: int
    body: dict or bytes

    def __post_init__(self):
        """
        Converts the body to bytes if it is a dictionary.
        """
        self.body = json.dumps(self.body).encode('utf-8')

    async def send_response(self, send) -> None:
        """
        Sends the response to the client.
        :param send: send channel
        :return: None
        """
        await send({
            'type': 'http.response.start',
            'status': self.status_code,
            'headers': [
                [b'content-type', b'application/json'],
            ],
        })
        await send({
            'type': 'http.response.body',
            'body': self.body
        })
