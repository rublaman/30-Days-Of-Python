import requests
import pprint
url = 'https://restcountries.com/v3.1/all'  # countries api
response = requests.get(url)  # opening a network and fetching a data
print(response)  # response object
print(response.status_code)  # status code, success:200
countries = response.json()
# we sliced only the first country, remove the slicing to see all countries
pprint.pprint(countries[:1])
