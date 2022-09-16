# sets
it_companies = {'Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon'}

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
len(it_companies)
# Add 'Twitter' to it_companies
it_companies.add('Twitter')
# Insert multiple IT companies at once to the set it_companies
it_companies.update({'HP', 'Tata'})
# Remove one of the companies from the set it_companies
it_companies.pop()
# What is the difference between remove and discard

# Thow a KeyError if it doesn't exist
print(it_companies.remove('Cognizant'))
# If the item doesn't exist it throw a None
print(it_companies.discard('Cognizant'))
