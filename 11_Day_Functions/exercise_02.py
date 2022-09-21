# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
# The number of odds are 50.
# The number of evens are 51.

import math
import statistics


def evens_and_odds(n):
    even = list(range(0, n + 1, 2))
    odds = list(range(1, n + 1, 2))
    return ('Odds: {}\nEvens: {}'.format(len(odds), len(even)))


print(evens_and_odds(100))

# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number.


def factorial(n):
    res = 1
    for i in range(1, n+1):
        res = res * i
    return res


print(factorial(7))

# Call your function is_empty, it takes a parameter and it checks if it is empty or not


def is_empty(value):
    if value == "" or len(value) == 0:
        return "It's empty"
    else:
        return "It's not empty"


print(is_empty(''))

# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std(standard deviation).

number_list = [1, 4, 2, 7, 3, 8, 2]


def calculate_mean(data):
    res = 0
    for n in data:
        res += n
    return res / len(data)


def calculate_median(data):
    data.sort()
    if len(data) % 2 == 0:
        value_1 = data[len(data) // 2]
        value_2 = data[(len(data) // 2) - 1]
        return (data[value_1] + data[value_2]) / 2
    else:
        return data[len(data) // 2]


def calculate_mode(data):
    return statistics.mode(data)


def calculate_range(data):
    data.sort()
    return data[-1] - data[0]


def calculate_variance(data):
    sum = 0
    mean = calculate_mean(data)
    for n in data:
        sum += (n - mean)**2
    return sum / len(data)


def calculate_std(data):
    res = calculate_variance(data)
    return math.sqrt(res)


print(calculate_mean(number_list))

print(calculate_median(number_list))

print(calculate_mode(number_list))

print(calculate_range(number_list))

print(calculate_variance(number_list))

print(calculate_std(number_list))
