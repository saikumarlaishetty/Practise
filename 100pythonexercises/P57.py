import json
from pprint import pprint


with open('company1.json','r') as f:
    d= json.loads(f.read())

pprint(d)

