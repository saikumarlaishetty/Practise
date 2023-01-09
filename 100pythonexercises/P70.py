import requests
response = requests.get("http://www.pythonhow.com/data/universe.txt", headers = {'user-agent': 'customUserAgent'})
text = response.text
print(text)