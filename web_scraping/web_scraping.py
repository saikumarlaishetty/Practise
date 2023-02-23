# https://www.youtube.com/watch?v=gRLHr664tXA&list=PLzMcBGfZo4-lSq2IDrA6vpZEV92AmQfJK

# from bs4 import BeautifulSoup

# with open("index.html","r") as f:
#    doc = BeautifulSoup(f,"html.parser")

# print the html doc in readable pretty model.
# print(doc.prettify())

# find by tag name
# tag = doc.title
# print(tag)

# find the string inside the tag
# print(tag.string)

# We can modify the string in the tag
# tag.string = "Hello"
# print(tag)

# tag = doc.find("a")   # This gives first occurence of 'a' tag

# to find all the occurences of 'a' tag use find_all
# tags = doc.find_all("p")
# print(tags)

# how to access the nested tags and how  to print the inside tags
# tags = doc.find_all("p")[0]
# print(tags.find_all("b"))




#############################################################
######                  USING REQUESTS MODULE        ########
#############################################################

# Parsing website HTML
# https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product


from bs4 import BeautifulSoup
import requests
#url = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product"
url = "https://www.newegg.ca/gigabyte-geforce-rtx-3070-gv-n3070gaming-oc-8gd/p/N82E16814932449"
result = requests.get(url)

# print(result.text)

# Reading the result.text using beautiful soup to get the html document.
doc = BeautifulSoup(result.text,"html.parser")

#print(doc.prettify())


# ##### Beautiful soup is a tree like structure.

# Locating text
prices = doc.find_all(text="$")
parent = prices[0].parent
price = parent.find("strong")
print(price.string)