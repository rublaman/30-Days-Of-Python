# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
from cmath import pi, sqrt
import cmath


def add_two_number(a, b):
    return a + b

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.


def area_of_circle(r):
    return pi * r * r

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.


def add_all_nums(*args):
    numbers = all(ele.isdigit() for ele in args)
    if numbers == False:
        return "This list no contains only numbers"
    else:
        return sum(args)

# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.


def convert_celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.


def check_season(month):
    if month == 'September' or 'October' or 'November':
        return 'Autumn'
    elif month == 'December' or 'January' or 'February':
        return 'Winter'
    elif month == 'March' or 'April' or 'May':
        return 'Spring'
    elif month == 'June' or 'July' or 'August':
        return 'Summer'

# Write a function called calculate_slope which return the slope of a linear equation


def calculate_slope(x1, x2, y1, y2):
    return (y2 - y1) / (x2 - x1)

# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.


def solve_quadratic_eqn(a, b, c):
    s = (b**2) - (4*a*c)

    s1 = (-b-cmath.sqrt(s))/(2*a)
    s2 = (-b+cmath.sqrt(s))/(2*a)

    print('The solution are {0} and {1}'.format(s1, s2))

# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.


def print_list(list):
    for e in list:
        print(e)


# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array(use loops).
def reverse_list(list):
    for i in range(len(list) - 1, -1):
        print(i)


print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"]))
# ["C", "B", "A"]
# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items


def capitalize_list_items(list):
    list_upper = [name.capitalize() for name in list]
    return list_upper


# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(list: list, item):
    list.append(item)
    return list


food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
# ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
print(add_item(food_staff, 'Meat'))
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))

# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.


def remove_item(list: list, item):
    list.remove(item)
    return list


food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]

# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.


def sum_of_numbers(n):
    res = 0
    for i in range(n + 1):
        res += i
    return res


print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10))  # 55
print(sum_of_numbers(100))  # 5050

# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.


def sum_of_odds(*args):
    res = 0
    for n in range:
        if res / 2 != 0:
            res += n
    return res


# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that range.

def sum_of_odds(*args):
    res = 0
    for n in range:
        if res / 2 == 0:
            res += n
    return res
