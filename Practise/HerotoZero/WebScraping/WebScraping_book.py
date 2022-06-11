# Goal to get title every book with 2 star rating

import requests,bs4

#http://books.toscrape.com/catalogue/page-3.html

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
#print(base_url.format(2))

res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text,'lxml')
products = soup.select('.product_pod')
example = products[0]
#print(example)
# If a class name has some space then we need to fill the gap with .
# Like star-rating Three  and star-rating.Three
#print(example.select('.star-rating.Three'))

#print(example.select('a')[1]['title'])

two_star_titles = []
for n in range(1,51):
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(res.text,'lxml')
    books = soup.select('.product_pod')
    for book in books:
        if len(book.select('.star-rating.Two')) !=0:
            book_title = book.select('a')[1]['title']
            two_star_titles.append(book_title)


print(two_star_titles)
