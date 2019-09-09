import zlib
import json
import hashlib
import threading
import logging
import sys
from datetime import datetime
from socket import socket
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from utils import get_chunk
from protocol import make_request
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDesktopWidget, QTextEdit, QVBoxLayout, QLineEdit


class Application:
    def __init__(self, host, port, buffersize):
        self._host = host
        self._port = port
        self._buffersize = buffersize
        self._message_recieved = pyqtSignal
        self._sock = socket()

    def __enter__(self):
        self._sock.connect((self._host, self._port))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        message = 'Client shutdown'
        if exc_type:
            if not exc_type is KeyboardInterrupt:
                message = 'Client stopped with error'
        logging.info(message, exc_info=exc_val)
        self._sock.close()
        return True

    @property
    def message_recieved(self):
        return self._message_recieved

    def connect(self):
        self._sock.connect((self._host, self._port))

    def read(self):
        comporessed_response = self._sock.recv(self._buffersize)
        encrypted_response = zlib.decompress(comporessed_response)

        nonce, encrypted_response = get_chunk(encrypted_response, 16)
        key, encrypted_response = get_chunk(encrypted_response, 16)
        tag, encrypted_response = get_chunk(encrypted_response, 16)

        cipher = AES.new(key, AES.MODE_EAX, nonce)

        raw_response = cipher.decrypt_and_verify(encrypted_response, tag)
        self._message_recieved.emit(json.loads(raw_response))
        logging.info(raw_response.decode())

    def write(self):
        key = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_EAX)

        hash_obj = hashlib.sha256()
        hash_obj.update(
            str(datetime.now().timestamp()).encode()
        )

        action = input('Enter action: ')
        data = json.loads(input('Enter data: '))

        request = make_request(action, data, hash_obj.hexdigest())
        bytes_request = json.dumps(request).encode()
        encrypted_request, tag = cipher.encrypt_and_digest(bytes_request)

        bytes_request = zlib.compress(
            b'%(nonce)s%(key)s%(tag)s%(data)s' % {
                b'nonce': cipher.nonce, b'key': key, b'tag': tag, b'data': encrypted_request
            }
        )
        self._sock.send(bytes_request)

    def render(self):
        app = QApplication(sys.argv)
        window = QMainWindow()
        window.setGeometry(400, 600, 400, 600)

        central_widget = QWidget()

        display_text = QTextEdit()
        display_text.setReadOnly(True)
        enter_text = QLineEdit()

        base_layout = QVBoxLayout()
        base_layout.addWidget(display_text)
        base_layout.addWidget(enter_text)

        central_widget.setLayout(base_layout)
        window.setCentralWidget(central_widget)

        dsk_widget = QDesktopWidget()
        geometry = dsk_widget.availableGeometry()
        center_position = geometry.center()
        frame_geometry = window.frameGeometry()
        frame_geometry.moveCenter(center_position)
        window.move(frame_geometry.topLeft())

        window.show()
        sys.exit(app.exec())

    def run(self):
        read_thread = threading.Thread(target=self.read)
        read_thread.start()

        self.render()
