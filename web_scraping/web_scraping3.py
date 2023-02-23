from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result,"html.parser")

#tbody = doc.tbody

# To get the contents or to get the list of all the tags inside the tbody
# trs = tbody.contents
#print(trs)

# Tree siblings
# To get the next sibling
# print(trs[0].next_sibling)

# To get the previous sibling
# print(trs[1].previous_sibling)

# To get the next siblings
# print(trs[0].next_siblings)      # this will generate a generator object
# print(list(trs[0].next_siblings))

# Tree parents and descendents
# Tree parents
# print(trs[0].parent)

# Tree descendants or contents or children
# print(trs[0].descendants)     #Generates a generator object

# print(list(trs[0].descendants))

# print(list(trs[0].contents))

#print(list(trs[0].children))

# Getting crypto prices
tbody = doc.tbody
trs = tbody.contents
prices = {}
#
# for tr in trs:
#     for td in tr.contents[2:4]:
#         print(td)
#         print()


for tr in trs[:10]:
    name, price = tr.contents[2:4]
    fixed_name = name.p.string
    fixed_price = price.a.string
    prices[fixed_name] = fixed_price

print(prices)