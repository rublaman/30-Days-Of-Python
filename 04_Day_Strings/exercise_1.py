# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
first_string = 'Thirty'
second_string = 'Days'
third_string = 'Of'
fourth_string = 'Python'
space = ' '
full_string = first_string + space + second_string + \
    space + third_string + space + fourth_string
# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
coding_string = 'Coding'
for_string = 'For'
all_string = 'All'
space = ' '
full_string = coding_string + space + for_string + space + all_string
# Declare a variable named company and assign it to an initial value "Coding For All".
company = full_string
# Print the variable company using print().
print(company)
# Print the length of the company string using len() method and print().
print(len(company))
# Change all the characters to uppercase letters using upper() method.
print(company.upper())
# Change all the characters to lowercase letters using lower() method.
print(company.lower())
# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())
# Cut(slice) out the first word of Coding For All string.
print(company[:6])
# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index('Coding'))

if 'Coding' in company:
    print('True')
# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding", "Coding For All"))
# Change Python for Everyone to Python for All using the replace method or other methods.
print(company.replace("Python", "everyone to Python for All"))
# Split the string 'Coding For All' using space as the separator (split()).
print("Coding For All".split())
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(','))
# What is the character at index 0 in the string Coding For All.
print('Coding For All'.find('Coding'))
# What is the last index of the string Coding For All.
print(len('Coding For All') - 1)
# What character is at index 10 in "Coding For All" string.
print('Coding For All'[10])
# Create an acronym or an abbreviation for the name 'Python For Everyone'.
print('Python For Everyone')
# Create an acronym or an abbreviation for the name 'Coding For All'.
print(''.join(e[0] for e in 'Coding For All'.split()))
# Use index to determine the position of the first occurrence of C in Coding For All.
print('Coding For All'.index('C'))
# Use index to determine the position of the first occurrence of F in Coding For All.
print('Coding For All'.index('F'))
# Use rfind to determine the position of the last occurrence of l in Coding For All People.
print('Coding For All People'.rfind('l'))
# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))
# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Does ''Coding For All' start with a substring Coding?
# Does 'Coding For All' end with a substring coding?
# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
# Which one of the following variables return True when we use the method isidentifier():
#   30DaysOfPython
#   thirty_days_of_python
# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
# Use the new line escape sequence to separate the following sentences.
#   I am enjoying this challenge.
#   I just wonder what is next.
# Use a tab escape sequence to write the following lines
#   Name      Age     Country   City
#   Asabeneh  250     Finland   Helsinki
# Use the string formatting method to display the following:
#   radius = 10
#   area = 3.14 * radius ** 2
#   The area of a circle with radius 10 is 314 meters square.
# Make the following using string formatting methods:
#   8 + 6 = 14
#   8 - 6 = 2
#   8 * 6 = 48
#   8 / 6 = 1.33
#   8 % 6 = 2
#   8 // 6 = 1
#   8 ** 6 = 262144
