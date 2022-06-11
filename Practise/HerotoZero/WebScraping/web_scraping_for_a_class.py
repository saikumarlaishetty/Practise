import requests
import bs4

res = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")
soup = bs4.BeautifulSoup(res.text,'lxml')

first_item = soup.select('.toctext')[0]
#print(first_item.text)

for item in soup.select('.toctext'):
    print(item.text)


