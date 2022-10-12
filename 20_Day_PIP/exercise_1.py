'''
1. Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
'''

import pprint
from statistics import median
import requests
from collections import Counter
import numpy as np

# url = 'http://www.gutenberg.org/files/1112/1112.txt'

# response = requests.get(url)
# words = response.text.split()
# top_words = Counter(words).most_common(10)
# print(top_words)


'''
2. Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find:
    the min, max, mean, median, standard deviation of cats' weight in metric units.
    the min, max, mean, median, standard deviation of cats' lifespan in years.
    Create a frequency table of country and breed of cats
'''


def get_weights(url):
    response_cat = requests.get(url)
    cats_res_json = response_cat.json()

    weights = []
    cleaned = []

    weights = list(cat['weight']['metric'] for cat in cats_res_json)
    aux = list([s.replace(' - ', '') for s in weights])
    cleaned = list(int(e[1:]) - int(e[0]) for e in aux)

    print(f'Min: {min(cleaned)}\nMax: {max(cleaned)}\nMedian: {median(cleaned)}\nStandard deviation: {np.std(cleaned)}')


# get_weights('https://api.thecatapi.com/v1/breeds')


def get_life_span(url):
    response_cat = requests.get(url)
    cats_res_json = response_cat.json()

    life_span = list(cat['life_span'] for cat in cats_res_json)
    cleaned = list([(int(e[e.find('-') + 2:]) +
                   int(e[0:e.find('-'):])) / 2 for e in life_span])

    print(f'Min: {min(cleaned)}\nMax: {max(cleaned)}\nMedian: {median(cleaned)}\nStandard deviation: {np.std(cleaned)}')


# get_life_span('https://api.thecatapi.com/v1/breeds')


'''
3. Read the countries API and find
the 10 largest countries
the 10 most spoken languages
the total number of languages in the countries API
'''


def get_largest_countries(url):
    response_cat = requests.get(url)
    res_countries = response_cat.json()

    populated = {}
    for country in res_countries:
        populated[country['name']['common']] = country['population']

    populated = sorted(populated.items(), key=lambda x: x[1], reverse=True)
    sortdict = dict(populated)

    print(list(sortdict.items())[:10])


# get_largest_countries('https://restcountries.com/v3.1/all')


def get_top_languages(url):
    response_cat = requests.get(url)
    res_countries = response_cat.json()
    lang = []

    for country in res_countries:
        if 'languages' in country:
            pprint.pprint(country['languages'])
            for language in country['languages']:
                print(language)
                lang.append(language)

    a_counter = Counter(lang)
    print(a_counter.most_common(10))


get_top_languages('https://restcountries.com/v3.1/all')


'''
4. UCI is one of the most common places to get data sets for data science and machine learning.
Read the content of UCL(https: // archive.ics.uci.edu/ml/datasets.php). Without additional libraries
it will be difficult, so you may try it with BeautifulSoup4

'''
