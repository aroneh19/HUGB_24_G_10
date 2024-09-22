import json

def load_json(file):
    with open(file, 'r') as file:
        return json.load(file)
