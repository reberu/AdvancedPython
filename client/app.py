import zlib
import json
import hashlib
import threading
from datetime import datetime
from socket import socket


class Application:
    def __init__(self, host, port, buffersize):
        self._host = host
        self._port = port
        self._buffersize = buffersize

        self._sock = socket()

    def connect(self, backlog=5):
        self._sock.connect((self._host, self._port))

    def read(self):
        while True:
            comporessed_response = self._sock.recv(self._buffersize)
            b_response = zlib.decompress(comporessed_response)
            print(b_response.decode())

    def run(self):
        print(f'Client was started')
        try:
            read_thread = threading.Thread(
                target=self.read, args=(self._sock, self._buffersize,)
            )
            read_thread.start()

            while True:
                hash_obj = hashlib.sha256()
                hash_obj.update(
                    str(datetime.now().timestamp()).encode()
                )

                action = input('Enter action: ')
                data = input('Enter data: ')

                request = {
                    'action': action,
                    'time': datetime.now().timestamp(),
                    'data': data,
                    'token': hash_obj.hexdigest()
                }

                s_request = json.dumps(request)
                b_request = zlib.compress(s_request.encode())
                self._sock.send(b_request)
                print(f'Client send data: {data}')

        except KeyboardInterrupt:
            self._sock.close()
            print('Client shutdown')
