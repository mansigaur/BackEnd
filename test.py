#testfile

import requests
from bs4 import BeautifulSoup as bs

url  = "https://news.yahoo.com/moscow-officials-urge-putin-gtfo-030517069.html"
# Getting response and creating soup object
resp = requests.get(url)
soup = bs(resp.text, 'html5lib')

# Using CSS selector extracting the author name 
author_tags = soup.find('div', {"class": "caas-attr-item-author"}).text
#caas-art-5cef1181-cba1-3edb-8e81-5b5b382d6576 > article > div > div > div > div > div.caas-content.wafer-sticky.wafer-loader-success > div.caas-content-wrapper > div:nth-child(2) > div.caas-attr > div > div.caas-attr-item-author > span
if author_tags != None and len(author_tags) == 1:
# author_tag.text return the "By Author Name"
# Splitting the data based on "By " and -1 return the last value from list

    author_name = author_tags[0].text.split('By ')[-1]