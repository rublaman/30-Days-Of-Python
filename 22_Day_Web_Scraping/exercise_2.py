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

list_scraping = []

for tr in table.find_all("tr"):
    res = tr.text.replace(u'\xa0', u' ').split('\n')
    if len(res) == 11:
        res_dict = {'Name': res[1], 'Data Types': res[3],
                    'Default Task': res[4], 'Attribute Types': res[5],
                    'Instances': res[6], 'Attributes': res[7], 'Year': res[8]}
        list_scraping.append(res_dict)

with open("./datasets.json", "w") as final:
    json.dump(list_scraping, final)


# for row in table.find_all('tr'):
#     # Find all data for each column
#     columns = row.find_all('td')
#     print(columns[0].text)

# for row in table.find_all('tr'):
#     value = row.find_all('td')
#     beautified_value = [ele.text.strip() for ele in value]
#     print(beautified_value)
