"""
  Check the data type of all your variables using type() built-in function
  Using the len() built-in function, find the length of your first name
  Compare the length of your first name and your last name
  Declare 5 as num_one and 4 as num_two
  Add num_one and num_two and assign the value to a variable total
  Subtract num_two from num_one and assign the value to a variable diff
  Multiply num_two and num_one and assign the value to a variable product
  Divide num_one by num_two and assign the value to a variable division
  Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
  Calculate num_one to the power of num_two and assign the value to a variable exp
  Find floor division of num_one by num_two and assign the value to a variable floor_division
  The radius of a circle is 30 meters.
  Calculate the area of a circle and assign the value to a variable name of area_of_circle
  Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
  Take radius as user input and calculate the area.
  Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
"""

from cmath import pi
from math import radians


first_name = "Ruben"
last_name = "Blanco"
full_name = "Ruben Blanco"
country = "Spain"
city = "Leon"
age = "29"
year = "2022"
is_married = False
is_ligth = True

# Using the len() built-in function, find the length of your first name
print(len(first_name))
# Compare the length of your first name and your last name
print("First name: ", len(first_name), "Las name: ", len(last_name))
# Declare 5 as num_one and 4 as num_two
num_one, num_two = 5, 4
# Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print(total)
# Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
print(diff)
# Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two
print(product)
# Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
print(division)
# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_one % num_two
print(remainder)
# Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
print(exp)
# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print(floor_division)
# The radius of a circle is 30 meters.
radius = 30 / (2 * pi)
print(radius)
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = pi * (radius ** 2)
print(area_of_circle)
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * pi * radius
print(circum_of_circle)
# Take radius as user input and calculate the area.
res = int(input("Insert a radius: "))
area = pi * (res ** 2)
print(area)
# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
