import json
import requests
import time

response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
time.sleep(3)

print(response)
time.sleep(2)

todos = json.loads(response.text)

time.sleep(4)
print(type(todos))

time.sleep(3)
print(todos)