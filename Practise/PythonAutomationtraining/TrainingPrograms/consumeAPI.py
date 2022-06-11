import requests
url = "http://127.0.0.1:5000"
resp = requests.get(url)
print(resp.text)