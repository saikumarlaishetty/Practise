import requests
result = requests.get("http://www.example.com")
print(type(result))

#print(result.text)

import bs4
soup = bs4.BeautifulSoup(result.text,"lxml")
#print(soup)
#print(soup.select('title))
title_tag =soup.select('title')
title_tag[0]
type(title_tag[0])
print(soup.select('title')[0].getText())