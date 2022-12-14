'''
Write a function which count number of lines and number of words in a text. All the files are in the data the folder:
    a) Read obama_speech.txt file and count number of lines and words
    b) Read michelle_obama_speech.txt file and count number of lines and words
    c) Read donald_speech.txt file and count number of lines and words
    d) Read melina_trump_speech.txt file and count number of lines and words
'''


import json
import re
from collections import Counter


def number_lines_words(path: str):
    with open(path) as f:
        lines = len(f.readlines())
        f.seek(0)
        txt = f.read()
        number_words = len(re.findall(r'[A-Za-z]+', txt))

    return (f'Number of lines: {lines} and number of words: {number_words}')


print(number_lines_words('../../data/obama_speech.txt'))
print(number_lines_words('../../data/michelle_obama_speech.txt'))
print(number_lines_words('../../data/donald_speech.txt'))
print(number_lines_words('../../data/melina_trump_speech.txt'))

'''
Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages

# Your output should look like this
print(most_spoken_languages(filename='./data/countries_data.json', 10))
    [(91, 'English'),
    (45, 'French'),
    (25, 'Arabic'),
    (24, 'Spanish'),
    (9, 'Russian'),
    (9, 'Portuguese'),
    (8, 'Dutch'),
    (7, 'German'),
    (5, 'Chinese'),
    (4, 'Swahili'),
    (4, 'Serbian')]

    # Your output should look like this
    print(most_spoken_languages(filename='./data/countries_data.json', 3))
    [(91, 'English'),
    (45, 'French'),
    (25, 'Arabic')]

'''


def most_spoken_languages(path: str, num: int):
    f = open(path, encoding="utf8")
    data = json.load(f)
    lang = []
    for country in data:
        for language in country['languages']:
            lang.append(language)

    a_counter = Counter(lang)
    return a_counter.most_common(num)


print(most_spoken_languages('../../data/countries_data.json', 3))


'''
Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries

# Your output should look like this
print(most_populated_countries(filename='./data/countries_data.json', 10))

    [
    {'country': 'China', 'population': 1377422166},
    {'country': 'India', 'population': 1295210000},
    {'country': 'United States of America', 'population': 323947000},
    {'country': 'Indonesia', 'population': 258705000},
    {'country': 'Brazil', 'population': 206135893},
    {'country': 'Pakistan', 'population': 194125062},
    {'country': 'Nigeria', 'population': 186988000},
    {'country': 'Bangladesh', 'population': 161006790},
    {'country': 'Russian Federation', 'population': 146599183},
    {'country': 'Japan', 'population': 126960000}
    ]

    # Your output should look like this

    print(most_populated_countries(filename='./data/countries_data.json', 3))
    [
    {'country': 'China', 'population': 1377422166},
    {'country': 'India', 'population': 1295210000},
    {'country': 'United States of America', 'population': 323947000}
    ]
'''


def most_populated_countries(path: str, num: int):
    f = open(path, encoding="utf8")
    data = json.load(f)

    populated = {}
    for country in data:
        populated[country['name']] = country['population']

    print(populated)

    populated = sorted(populated.items(), key=lambda x: x[1], reverse=True)
    sortdict = dict(populated)

    return dict(list(sortdict.items())[:num])


print(most_populated_countries('../../data/countries_data.json', 3))
