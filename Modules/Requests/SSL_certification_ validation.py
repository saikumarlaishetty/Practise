# import requests module
import requests

# Making a get request
response = requests.get('https://expired.badssl.com/')

# print request object
print(response)