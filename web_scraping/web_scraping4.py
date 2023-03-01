# Finding the best GPU prices
# https://www.youtube.com/watch?v=zAEfWiC_KBU&list=PLzMcBGfZo4-lSq2IDrA6vpZEV92AmQfJK&index=4

from bs4 import BeautifulSoup
import re
import requests


search_term = input("What product do you want to search for ?")

url = f"https://www.newegg.ca/p/pl?d={search_term}&N=4131"
page = requests.get(url).text
doc = BeautifulSoup(page,"html.parser")

page_text = doc.find(class_='list-tool-pagination-text').strong
# print(page_text)

pages = int(str(page_text).split("/")[-2].split('>')[-1][:-1])
# print(pages)

items_found = {}

for page in range(1,pages+1):
    url = f"https://www.newegg.ca/p/pl?d={search_term}&N=4131&page={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

    div = doc.find(class_= "item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")

    items = div.find_all(text=re.compile(search_term))     # if you just use text = "gpu" it will only match "gpu" but not "gpu oo1"
                                                            # so we are using a re.compile to match both "gpu" and "gpu 001"

    import pdb
    pdb.set_trace()
    for item in items:
        parent = item.parent
        link = None
        if parent.name != "a":
            continue

        link = parent['href']
        next_parent = item.find_parent(class_='item-container')
        try:
            price = next_parent.find(class_="price-current").find("strong").string
            items_found[item] ={"price":int(price.replace(",","")),"link":link}
        except:
            pass


# print(items_found)


# Sorting products by price
sorted_items = sorted(items_found.items(),key= lambda x:x[1]['price'])

for item in sorted_items:
    print(item[0])
    print(f"${item[1]['price']}")
    print(item[1]['link'])
    print("------------------------")



