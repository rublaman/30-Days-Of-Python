# Create an empty tuple
from unicodedata import name


empty_tuple = ()
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
names_familiy = ('Marta', 'Ruben')
# Join brothers and sisters tuples and assign it to siblings
brothers = ('Ruben',)
sisters = ('Marta',)
siblings = brothers + sisters
# How many siblings do you have?
print(siblings)
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
names_familiy = list(names_familiy)
names_familiy.extend(['Cipri', 'Esther'])
family_members = tuple(names_familiy)
print(family_members)
