# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.
age = int(input('Enter your age: '))
print('You are old enough to drive') if age >= 18 else print(
    'Yo have to wait: {} year(s) to drive'.format(18 - age))

# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
# Enter your age: 30
# You are 5 years older than me.
your_age = int(input('Enter your age: '))
my_age = 29

if your_age == my_age:
    print('We have the same age')
elif your_age >= my_age:
    if your_age - my_age == 1:
        print('You are just one year olden than me')
    else:
        print('You are {} years older than me'.format(your_age - my_age))
else:
    if my_age - your_age == 1:
        print('I\'m just one year olther than you')
    else:
        print('I\'m {} years older than you'.format(my_age - your_age))
