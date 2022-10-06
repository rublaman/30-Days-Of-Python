from countries_data import countries_data
from pprint import pprint
from collections import Counter
# Use the countries_data.py(https: // github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
# Sort countries by name, by capital, by population


def sort_by_name(data):
    return sorted(data, key=lambda d: d['name'])


def sort_by_capital(data):
    return sorted(data, key=lambda d: d['capital'])


def sort_by_population(data):
    return sorted(data, key=lambda d: d['population'], reverse=True)


# Sort out the ten most spoken languages by location.

res = [cto for country in countries_data for cto in country['languages']]
a_counter = Counter(res)

# Sort out the ten most populated countries.


def sort_by_population_and_num(data, num):
    return sorted(data, key=lambda d: d['population'], reverse=True)[:num]


pprint(sort_by_population_and_num(countries_data, 10))
