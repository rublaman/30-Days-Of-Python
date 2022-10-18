'''
Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').
'''

import requests
from bs4 import BeautifulSoup
import json
import pprint
url = 'http://www.bu.edu/president/boston-university-facts-stats/'

res = requests.get(url)
content = res.content
status = res.status_code
print(status)

soup = BeautifulSoup(content, 'html.parser')
print(soup.title.getText())
sections = soup.find_all('div', {'class': 'facts-wrapper'})

list_scraping = []

for section in sections:
    header = section.find('h5').text
    res = {'Section': header, 'Categories': {}}
    for li in section.find('ul'):
        categories = li.text.split("\n")
        if categories[1] != '':
            res['Categories'][categories[1]] = categories[2]
    list_scraping.append(res)

with open("./mydata.json", "w") as final:
    json.dump(list_scraping, final)
