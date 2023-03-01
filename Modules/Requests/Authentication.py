# Authentication using python requests

import requests
from requests.auth import HTTPBasicAuth

"""
To achieve this authentication, typically one provides authentication data through Authorization header or a custom header defined by server.
 
"""


response = requests.get('https://api.github.com/',auth = HTTPBasicAuth('user','pass'))

print(response)