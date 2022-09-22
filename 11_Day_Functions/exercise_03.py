import collections
from doctest import REPORTING_FLAGS
import countries_data

# Write a function called is_prime, which checks if a number is prime.
from keyword import iskeyword


def is_prime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return "It's not prime"
        return "It's prime"


print(is_prime(29))

# Write a functions which checks if all items are unique in the list.


def unique_list(list: list):
    check_list = []
    if len(list) >= 1:
        for i in list:
            if i in check_list:
                return "This list is not unique"
            else:
                check_list.append(i)
        return "This list contain unique items"


print(unique_list([1, 2, 2, 4, 5]))
# Write a function which checks if all the items of the list are of the same data type.


def check_list_same_type(list: list):
    if len(list) >= 1:
        check_list = type(list[0])
        for i in list:
            if type(i) != check_list:
                return "This list has different data types"
        return "THis list has the same data type"


print(check_list_same_type([1, 2, 2, "4", 5]))


# Write a function which check if provided variable is a valid python variable

def check_variable(var):
    if var.isidentifier() and not iskeyword(var):
        return 'It\'s valid'
    else:
        return "It's not valid"


print(check_variable("while"))

# Go to the data folder and access the countries-data.py file.
# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order


def most_spoken_languages(list: list):
    countries = []
    for country in list:
        for cto in country['languages']:
            countries.append(cto)

    a_counter = collections.Counter(countries)
    return a_counter.most_common()[10:20]


print(most_spoken_languages(countries_data.contries_data))

# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.


def most_populated_contries(list_of_countries: list):
    populated = {}
    for country in list_of_countries:
        populated[country['name']] = country['population']

    populated = sorted(populated.items(), key=lambda x: x[1], reverse=True)
    return populated[10:20]


print(most_populated_contries(countries_data.contries_data))
