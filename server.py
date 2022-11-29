import socket
import logging

log = logging.getLogger(__name__)


class Server:
    def __init__(self, host: str, port: int):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port

    def start(self):

        log.info(f'Starting server on port {self.port}')

        self.sock.bind((self.host, self.port))
        self.sock.listen()
        conn, addr = self.sock.accept()
        with conn:
            log.info(f'Connected by device {addr[0]} from port {addr[1]}')
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                log.info(f'Received data: {data}')
                conn.sendall(data)

    def close(self):
        log.info(f'Closing server')
        self.sock.close()
