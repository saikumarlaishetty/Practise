# letter counter

import requests

response = requests.get("http://www.pythonhow.com/data/universe.txt")

text = response.text
print(text.count('a'))