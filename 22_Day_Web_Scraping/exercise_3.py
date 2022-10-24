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
table = soup.find('table', {'class': 'wikitable'})
table_body = table.find('tbody')

list_scraping = []

for tr in table_body.find_all("tr")[1:]:
    res = tr.text.replace(u'\xa0', u' ').split('\n')
    res_dict = {'No': res[1], 'Name': res[5],
                'Term': res[7], 'Party': res[11], 'Election': res[13], 'VicePresident': res[15]}
    list_scraping.append(res_dict)

with open("./presidents.json", "w") as final:
    json.dump(list_scraping, final)
