# Explain the difference between map, filter, and reduce.
# Explain the difference between higher order function, closure and decorator
# Define a call function before map, filter or reduce, see examples.
# Use for loop to print each country in the countries list.
# Use for to print each name in the names list.
# Use for to print each number in the numbers list.
# Explain the difference between map, filter, and reduce.
'''
MAP

It's a incorpored function that takes a function as a parameter
and a iterable as a second param.

FILTER
It's a specific function that return a boolean for each item in 
the iterable. Filter the elements when the filter is right.

REDUCE
It's a functools modules. It takes two paramateres. The first one
is a function and the second one is a iterable. Unlike map or filter,
reduce returns just one value.

'''

# Explain the difference between higher order function, closure and decorator
'''
HIGHER ORDER FUNCTION
It's called a higher order function if it contains other functions
as a paramter or returns a function as an output.

We can store the function in a variable
We can pass the function as a paramter to another function
We can return the function from a function
We can store them in data structures such as hash tables, list, etc...

CLOSURE
A inner function can access to the external scope.

DECORATOR
A decorator takes in a function, adds some functionality and returns it.

'''
# Define a call function before map, filter or reduce, see examples.


from functools import reduce
nums = [1, 2, 3, 4, 5]


def multiply_by_two(x):
    return x * 2


def is_odd(x):
    return True if x % 2 == 0 else False


def sum_nums(x, y):
    return x + y


res_map = map(multiply_by_two, nums)
print(list(res_map))

res_filter = filter(is_odd, nums)
print(list(res_filter))

res_reduce = reduce(sum_nums, nums)
print(res_reduce)


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use for loop to print each country in the countries list.
list(map(print, countries))
# Use for to print each name in the names list.
lambda x: print(x), names
# Use for to print each number in the numbers list.
list(map(print, numbers))
