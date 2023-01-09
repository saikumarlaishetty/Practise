import requests
import bs4

#url = "http://quotes.toscrape.com/"

class webScrape:
    def __int__(self, url, text=None,lasttext = None):
        self.url = url
        self.text = text
        self.lasttext = lasttext

    def scrape_to_text(self,page=None):
        if page is not None:
            res = requests.get((self.url).format(page))
        else:
            res = requests.get(self.url)
        soup = bs4.BeautifulSoup(res.text,"lxml")
        return soup

    def get_list(self):
        soup = webScrape.scrape_to_text()
        lists = soup.select(self.text)
        temp_list = []
        for temp in lists:
            temp_list.append(temp.getText())

        return temp_list

    def scrape_all_pages(self):
        while True:
            page = 1
            soup = webScrape.scrape_to_text(page)
            temp = webScrape.get_list()
            if "No quotes found!" in soup.select("."+self.lasttext)[1].getText():
                break
            page = page + 1

            return set(temp)


if __name__ == "__main__":
    # Task1
    url = "http://quotes.toscrape.com/"
    #ws = webScrape(url,text = "author")
    ws = webScrape()
    souptext = ws.scrape_to_text()
    auth_list = ws.get_list()
    print(set(auth_list))
