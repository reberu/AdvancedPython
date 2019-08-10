import yaml
import json
import logging
from log.client_log_config import add_info
from socket import socket
from datetime import datetime
from argparse import ArgumentParser


parser = ArgumentParser()

parser.add_argument(
    '-c', '--config', type=str,
    required=False, help='Sets config file path'
)

args = parser.parse_args()

default_config = {
    'host': 'localhost',
    'port': 8000,
    'buffersize': 1024
}

if args.config:
    with open(args.config) as file:
        file_config = yaml.load(file, Loader=yaml.Loader)
        default_config.update(file_config)

sock = socket()
sock.connect(
    (default_config.get('host'), default_config.get('port'))
)

add_info(f'Client was started')

action = input('Enter action: ')
data = input('Enter data: ')

request = {
    'action': action,
    'time': datetime.now().timestamp(),
    'data': data
}

s_request = json.dumps(request)

sock.send(s_request.encode())
add_info(f'Client send data: {data}')
b_response = sock.recv(default_config.get('buffersize'))
add_info(b_response.decode())
