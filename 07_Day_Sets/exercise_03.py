age = [22, 19, 24, 25, 26, 24, 25, 24]
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
print('Length of age list: ', len(age))
age = set(age)
print('Length of age set: ', len(age))
# Explain the difference between the following data types: string, list, tuple and set
#   String is a type of data, is a chain of characteres between comas.
#   A list is an ordered and mutable type of collection
#   A tuple is an ordered and inmutable type of collection
#   A set is an unordered, un-indexed type of collection with unique items
# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
str = 'I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence?'
words = str.split()
words = set(words)
print(len(words))
