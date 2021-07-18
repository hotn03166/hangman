# pip install beautifulsoup4==4.6.0

import os
import urllib.request
from bs4 import BeautifulSoup

class Scraper:

    urls = []
    
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = 'html.parser'
        sp = BeautifulSoup(html, parser)

        for tag in sp.find_all('a'):
            url = tag.get('href')
            if url is None:
                continue
            else:
                self.urls.append(url)

def write_file(urls):
    os.path.join('python_ws', 'hangman', 'web_scraper')

    with open('output_urls.txt', 'w', encoding='utf-8') as f:
        for url in urls:
            f.write('\n' + url)


news = 'https://news.google.com/'
sc = Scraper(news)
sc.scrape()

write_file(sc.urls)



