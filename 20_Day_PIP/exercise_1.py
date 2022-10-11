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

    for cat in cats_res_json:
        weights.append(cat['weight']['metric'])

    aux = list([s.replace(' - ', '') for s in weights])
    cleaned = list(int(e[1:]) - int(e[0]) for e in aux)

    print(f'Min: {min(cleaned)}\nMax: {max(cleaned)}\nMedian: {median(cleaned)}\nStandard deviation: {np.std(cleaned)}')


get_weights('https://api.thecatapi.com/v1/breeds')


'''
3. Read the countries API and find
the 10 largest countries
the 10 most spoken languages
the total number of languages in the countries API
'''

'''
4. UCI is one of the most common places to get data sets for data science and machine learning.
Read the content of UCL(https: // archive.ics.uci.edu/ml/datasets.php). Without additional libraries
it will be difficult, so you may try it with BeautifulSoup4

'''
