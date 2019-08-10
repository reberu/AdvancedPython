import yaml

data = {
    1: [1, 2, 3, 4, 5],
    2: 42,
    3: {1010: 'Є'}
}

with open('file.yaml', 'w') as file:
    yaml.dump(data, file, default_flow_style=True, allow_unicode=True)
