import collections
from distutils.command.build_scripts import first_line_re
import countries
import countries_data


# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
for country in countries.countries:
    if 'land' in country:
        print(country)

# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruit = ['banana', 'orange', 'mango', 'lemon']
fruit.reverse()
print(fruit)

# Go to the data folder and use the countries_data.py file.
# What are the total number of languages in the data

countries = []
for country in countries_data.contries_data:
    for cto in country['languages']:
        if cto in countries:
            continue
        else:
            countries.append(cto)

print(len(countries))


countries.clear()
# Find the ten most spoken languages from the data

for country in countries_data.contries_data:
    for cto in country['languages']:
        print(cto)
        countries.append(cto)


a_counter = collections.Counter(countries)
print(a_counter.most_common(10))

# Find the 10 most populated countries in the world

populated = {}
for country in countries_data.contries_data:
    populated[country['name']] = country['population']


populated = sorted(populated.items(), key=lambda x: x[1], reverse=True)
sortdict = dict(populated)

res = dict(list(sortdict.items())[:10])
print(res)
