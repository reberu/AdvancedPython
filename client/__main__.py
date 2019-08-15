import yaml
from argparse import ArgumentParser
from app import Application


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

app = Application(
    default_config.get('host'),
    default_config.get('port'),
    default_config.get('buffersize'),
)

app.connect()
app.run()
