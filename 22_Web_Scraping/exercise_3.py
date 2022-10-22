'''
Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). The table is not very structured and the scrapping may take very long time.
'''

import requests
from bs4 import BeautifulSoup
import json
import pprint
url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'

res = requests.get(url)
content = res.content
status = res.status_code
print(status)

soup = BeautifulSoup(content, 'html.parser')
table = soup.find_all('table', {'class': 'wikitable'})

#
