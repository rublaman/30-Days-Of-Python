'''
Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file
'''

import requests
from bs4 import BeautifulSoup
import json
import pprint
url = 'https://archive.ics.uci.edu/ml/datasets.php'

res = requests.get(url)
content = res.content
status = res.status_code
print(status)

soup = BeautifulSoup(content, 'html.parser')
tables = soup.find_all('table', {'cellpadding': '3'})

table = tables[0]

for tr in table.find_all("tr"):
    print(tr.text.replace(u'\xa0', u' ').split('\n'))
    print('###')

# for row in table.find_all('tr'):
#     # Find all data for each column
#     columns = row.find_all('td')
#     print(columns[0].text)

# for row in table.find_all('tr'):
#     value = row.find_all('td')
#     beautified_value = [ele.text.strip() for ele in value]
#     print(beautified_value)
