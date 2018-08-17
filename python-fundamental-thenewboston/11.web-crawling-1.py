################# How to Build a Web Crawler  #############

import requests

from bs4 import BeautifulSoup

def trade_spider(max_pages):     #Main function which will go thru all 
    page = 1                     # Default we are restricting to crawl 1 page, we can restrict the count using "max_pages"
    while page <= max_pages:
        url = 'https://buckysroom.org/trade/search.php?page=' + str(page)
        source_code = requests.get(url)                       # Variable source code will hold all the contents
        plain_text = source_code.text                         # We are only care about the textual content of the page
        soup = BeautifulSoup(plain_text)                      # We passed all the contents from plain_text(source code) to soup object for further processing 
        for link in soup.findAll('a', {'class' : 'item-name'}):  # This will loop thru all the code and pick the links will class 'item-name'
            href = link.get('href')                            # Pull the link which is inside the href section
            href = "https://buckysroom.org/" +  link.get('href') 
            title = link.string                                #Pull only string part
            print(href)
            print(title)
        page =+ 1

trade_spider(1)
