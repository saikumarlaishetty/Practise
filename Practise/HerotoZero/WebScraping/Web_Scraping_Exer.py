import requests
import bs4



res = requests.get("http://quotes.toscrape.com/")
soup = bs4.BeautifulSoup(res.text,"lxml")

#print(soup)
#TASK: Get the names of all the authors on the first page.
authors = soup.select(".author")
#print(authors)
#print(soup.select(".author")[0].getText())
auth_list = []
for author in authors:
    auth_list.append(author.getText())

#print(set(auth_list))  # Author set

# Create a list of all the quotes on the first page.
quote_list = []
quotes = soup.select('.text')
#print(quotes[0].getText())
for quote in quotes:
   quote_list.append(quote.getText())

#print(quote_list)


"""
TASK: Inspect the site and use Beautiful Soup to extract the top ten tags from the requests text shown on the top right
from the home page (e.g Love,Inspirational,Life, etc...). HINT: Keep in mind there are also tags underneath each quote,
try to find a class only present in the top right tags, perhaps check the span.
"""
tags = soup.select('.tag-item')
#print(tags[0].getText())
for tag in tags:
    pass
    #print(tag)
    #print(tag.getText())

"""
TASK: Notice how there is more than one page, and subsequent pages look like this http://quotes.toscrape.com/page/2/. 
Use what you know about for loops and string concatenation to loop through all the pages and get all the unique authors 
on the website. Keep in mind there are many ways to achieve this, also note that you will need to somehow figure out 
how to check that your loop is on the last page with quotes. For debugging purposes, I will let you know that there are
only 10 pages, so the last page is http://quotes.toscrape.com/page/10/, but try to create a loop that is robust enough 
that it wouldn't matter to know the amount of pages beforehand, perhaps use try/except for this, its up to you!
"""

base_url = 'http://quotes.toscrape.com/page/{}/'

temp = 1
author_list = []
while True:
    res = requests.get(base_url.format(temp))
    soup = bs4.BeautifulSoup(res.text,'lxml')
    print(soup)
    authors = soup.select('.author')
    for author in authors:
        author_list.append(author.getText())

    temp = temp+1
    print("++++++++++++++")
    print(soup.select(".col-md-8")[1].getText())
    print("++++++++++++++")
    if "No quotes found!" in soup.select(".col-md-8")[1].getText():
        break
    print(temp)

print(set(author_list))
