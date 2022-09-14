# Declare an empty list
my_list = []
# Declare a list with more than 5 items
my_list2 = ["Hi", "my", "name is", "Ruben", 29]
# Find the length of your list
len(my_list2)
# Get the first item, the middle item and the last item of the list
my_list2[::2]
# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Ruben", 29, 203, "single", "Spain"]
# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft",
                "Apple", "IBM", "Oracle", "Amazon"]
# Print the list using print()
print(mixed_data_types)
# Print the number of companies in the list
print(it_companies)
# Print the first, middle and last company
print(it_companies[::3])
# Print the list after modifying one of the companies
it_companies[0] = "Meta"
print(it_companies)
# Add an IT company to it_companies
it_companies.append('NTT')
# Insert an IT company in the middle of the companies list
it_companies.insert(int((len(it_companies)) / 2), "Samsung")
print(it_companies)
# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()
print(it_companies)
# Join the it_companies with a string '#;  '
string_example = "#; "
it_companies.extend(string_example)
print(it_companies)
# Check if a certain company exists in the it_companies list.
print("IBM" in it_companies)
# Sort the list using sort() method
it_companies.sort()
print(it_companies)
# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)
# Slice out the first 3 companies from the list
print(it_companies[0:3])
# Slice out the last 3 companies from the list
print(it_companies[-4:-1])
# Slice out the middle IT company or companies from the list
print(it_companies[::2])
# Remove the first IT company from the list
del it_companies[0]
# Remove the middle IT company or companies from the list
del it_companies[:len(it_companies) // 2]
# Remove the last IT company from the list
del it_companies[-1]
# Remove all IT companies from the list
it_companies.clear()
# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
front_end.extend(back_end)
# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux
full_stack = front_end.copy()
after_redux = full_stack.index('Redux')
full_stack.insert(after_redux + 1, "Python")
full_stack.insert(after_redux + 1, "SQL")
print(full_stack)
