'''
Clean the following text. After cleaning, count three most frequent words in the string.
'''

import string


sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''


def clean_text(text: string):
    pass


print(clean_text(sentence))
# I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher


def most_frequent_words(text: string):
    pass


print(most_frequent_words(cleaned_text))
# [(3, 'I'), (2, 'teaching'), (2, 'teacher')]
