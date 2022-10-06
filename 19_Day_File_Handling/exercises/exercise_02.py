
from collections import Counter
from difflib import SequenceMatcher
import re
import csv


'''
Extract all incoming email addresses as a list from the email_exchange_big.txt file.
'''

with open('../../data/email_exchanges_big.txt') as f:
    txt = f.read()
    email_matches = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', txt)

# print(len(email_matches))


'''
Find the most common words in the English language. Call the name of your function find_most_common_words,
it will take two parameters - a string or a file and a positive integer, indicating the number of words.
Your function will return an array of tuples in descending order. Check the output

   # Your output should look like this
    print(find_most_common_words('sample.txt', 10))
    [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
    (6, 'of'),
    (5, 'and'),
    (4, 'a'),
    (4, 'in'),
    (3, 'that'),
    (2, 'have'),
    (2, 'I')]

    # Your output should look like this
    print(find_most_common_words('sample.txt', 5))

    [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
    (6, 'of'),
    (5, 'and')]

'''


def find_most_common_words(path_file, num: int):
    with open(path_file) as f:
        txt = f.read()
        word_matches = re.findall(r'[A-Za-z]+', txt)
        w_counter = Counter(word_matches).most_common(num)
        print(w_counter)


find_most_common_words('../../data/email_exchanges_big.txt', 10)
'''
Use the function, find_most_frequent_words to find:
    a) The ten most frequent words used in Obama's speech
    b) The ten most frequent words used in Michelle's speech
    c) The ten most frequent words used in Trump's speech
    d) The ten most frequent words used in Melina's speech
'''

find_most_common_words('../../data/obama_speech.txt', 10)
find_most_common_words('../../data/michelle_obama_speech.txt', 10)
find_most_common_words('../../data/donald_speech.txt', 10)
find_most_common_words('../../data/melina_trump_speech.txt', 10)


'''
Write a python application that checks similarity between two texts. It takes a file or a string as a parameter
and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts
of Michelle's and Melina's speech. You may need a couple of functions, function to clean the text(clean_text),
function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity).
List of stop words are in the data directory
'''
stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up',
              'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]


def clean(path_file):
    with open(path_file) as f:
        txt = f.read()
        res = re.sub('[^A-Za-z0-9 ]+', '', txt)
        return res


def remove_support_words(text: str):
    list_words = text.split()
    filtered_text = [word for word in list_words if word.lower()
                     not in stop_words]
    return ' '.join(filtered_text)


def check_text_similarity(text_1: str, text_2: str):
    return SequenceMatcher(None, text_1, text_2).ratio()


melina_text = clean('../../data/melina_trump_speech.txt')
melina_cleaned = remove_support_words(melina_text)

michelle_text = clean('../../data/michelle_obama_speech.txt')
michelle_cleaned = remove_support_words(michelle_text)
print(michelle_cleaned)

print(check_text_similarity(michelle_cleaned, melina_cleaned))


'''
Find the 10 most repeated words in the romeo_and_juliet.txt
'''
find_most_common_words('../../data/romeo_and_juliet.txt', 10)

'''
Read the hacker news csv file and find out:
    a) Count the number of lines containing python or Python
    b) Count the number lines containing JavaScript, javascript or Javascript
    c) Count the number lines containing Java and not JavaScript
'''


def findWholeWord(w, cadena):
    # OPTION 1
    # return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search(cadena)
    # OPTION 2
    return re.search(r'\b({0})\b'.format(w), cadena, flags=re.IGNORECASE)


def count_number_words_csv(word: str, path: str):
    with open(path) as f:
        csv_reader = csv.reader(f, delimiter=',')
        count = 0

        for row in csv_reader:
            for e in row:
                if findWholeWord(word, e) is not None:
                    count += 1
                    continue

    return count


print(count_number_words_csv('Python', '../../data/hacker_news.csv'))
print(count_number_words_csv('JavaScript', '../../data/hacker_news.csv'))
print(count_number_words_csv('java', '../../data/hacker_news.csv'))
