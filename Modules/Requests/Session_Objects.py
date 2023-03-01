import requests

"""
Session object allows one to persist certain parameters across requests. It also persists cookies across all requests made 
from the Session instance and will use urllib3’s connection pooling. So if several
 requests are being made to the same host, the underlying TCP connection will be reused, which can result in a significant 
performance increase. A session object all the methods as of requests.

"""

import requests

# create a session object
s = requests.Session()

# make a get request
s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')

# again make a get request
r = s.get('https://httpbin.org/cookies')

# check if cookie is still set
print(r.text)