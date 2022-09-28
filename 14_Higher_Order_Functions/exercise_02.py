from countries import countries
from countries_data import countries_data
from functional import seq

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use map to create a new list by changing each country to uppercase in the countries list
upper_countrys = list(map(lambda c: c.upper(), countries))
# Use map to create a new list by changing each number to its square in the numbers list
square_number = list(map(lambda n: n ** 2, numbers))
# Use map to change each name to uppercase in the names list
upper_name = list(map(lambda name: name.upper(), names))
print(upper_name)
# Use filter to filter out countries containing 'land'.


def contains_land(country_name):
    return True if 'land' in country_name else False


countries_with_land = list(filter(contains_land, countries))
print(countries_with_land)
# Use filter to filter out countries having exactly six characters.


def six_characters(country_name):
    return True if len(country_name) == 6 else False


countries_with_six_chars = list(filter(six_characters, countries))
print(countries_with_six_chars)

# Use filter to filter out countries containing six letters and more in the country list.


def six_or_more_chars(country_name):
    return True if len(country_name) >= 6 else False


countries_with_six_chars = list(filter(six_or_more_chars, countries))
print(countries_with_six_chars)

# Use filter to filter out countries starting with an 'E'
countries_start_with_e = list(filter(lambda c: c.startswith('E'), countries))
print(countries_start_with_e)
# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
chained = seq(countries).map(lambda c: c.upper()
                             ).filter(lambda c: c.startswith('E'))

print(chained)
# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
# Use reduce to sum all the numbers in the numbers list.
# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
# Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
# Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
# Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
