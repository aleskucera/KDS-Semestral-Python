import socket
import logging

log = logging.getLogger(__name__)


class Client:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host, port):
        self.sock.connect((host, port))

    def send(self, data):
        log.info(f'Sending data: {data}')
        self.sock.sendall(data)

    def close(self):
        log.info(f'Closing the client')
        self.sock.close()
