'''
  Declare your age as integer variable
  Declare your height as a float variable
  Declare a variable that store a complex number
  Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle(area=0.5 x b x h).
  Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle(perimeter=a + b + c).
  Get length and width of a rectangle using prompt. Calculate its area(area=length x width) and perimeter(perimeter=2 x(length + width))
  Get radius of a circle using prompt. Calculate the area(area=pi x r x r) and circumference(c=2 x pi x r) where pi = 3.14.
  Slope is (m=y2-y1/x2-x1). Find the slope and Euclidean distance between point(2, 2) and point(6, 10)
  Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
  Find the length of 'python' and 'dragon' and make a falsy comparison statement.
  Use and operator to check if 'on' is found in both 'python' and 'dragon'
  I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
  There is no 'on' in both dragon and python
  Find the length of the text python and convert the value to float and convert it to string
  Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
  Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
  Check if type of '10' is equal to type of 10
  Check if int('9.8') is equal to 10
  Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
  Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
  Write a Python script that displays the following table:
    1 1 1 1 1
    2 1 2 4 8
    3 1 3 9 27
    4 1 4 16 64
    5 1 5 25 125
'''
# Declare your age as integer variable
from cmath import sqrt
from operator import length_hint


age = 25
print(type(age))
# Declare your height as a float variable
height = 2.03
print(type(height))
# Declare a variable that store a complex number
complex = 1 + 4j
print(type(complex))
# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle(area=0.5 x b x h).
height_triangle = int(input("Height of the triangle: "))
base_triangle = int(input("Base of the triangle: "))
print(0.5 * height_triangle * base_triangle)
# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle(perimeter=a + b + c).
side_a = int(input("Side a: "))
side_b = int(input("Side b: "))
side_c = int(input("Side c: "))
print(side_a + side_b + side_c)
# Get length and width of a rectangle using prompt. Calculate its area(area=length x width) and perimeter(perimeter=2 x(length + width))
length_rectangle = int(input("length rectangle: "))
width_rectangle = int(input("width rectangle: "))
print("Area of rectangle: ", length_rectangle * width_rectangle)
print("Perimeter of rectangle: ", 2 * (length_rectangle * width_rectangle))
# Get radius of a circle using prompt. Calculate the area(area=pi x r x r) and circumference(c=2 x pi x r) where pi = 3.14.
radius_circle = int(input("radius circle: "))
print("Area of circle", 3.14 * radius_circle * radius_circle)
print("Circunference of circle", 2 * 3.14 * radius_circle)
# Slope is (m=y2-y1/x2-x1). Find the slope and Euclidean distance between point(2, 2) and point(6, 10)
eucDistance = sqrt((6-2)**2+(10-2)**2)
print(eucDistance)
# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x = -3
y = (x**2 + 6*x + 9)
# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len('python') != len('dragon'))
# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python')
# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jargon' in 'I hope this course is not full of jargon')
# There is no 'on' in both dragon and python
print('on' in 'dragon' == 'on' in 'python')
# Find the length of the text python and convert the value to float and convert it to string
print(str(float(len("python"))))
# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
print(10 % 2)
# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7 / 3 == int(2.7))
# Check if type of '10' is equal to type of 10
print(type('10') == type(10))
# Check if int('9.8') is equal to 10
print(type('9.8') != type(10))
# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = int(input("number of hours: "))
rate_hour = int(input("rate per hour: "))
print(hours * rate_hour)
# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
age = int(input("age: "))
age_seconds = age * 31536000
hundred_years_seconds = 100 * 31536000
print(hundred_years_seconds - age_seconds)
# Write a Python script that displays the following table
print('1 1 1 1 1\n2 1 2 4 8\n3 1 3 9 27\n4 1 4 16 64\n5 1 5 25 125')
