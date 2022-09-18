# Write a code which gives grade to students according to theirs scores:
# 90-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F
score = int(input('Insert a score: '))
if score <= 100 and score >= 90:
    print('A')
elif score <= 89 and score >= 70:
    print('B')
elif score <= 69 and score >= 60:
    print('C')
elif score <= 59 and score >= 50:
    print('D')
elif score <= 49 and score >= 0:
    print('F')

# Check if the season is Autumn, Winter, Spring or Summer. If the user input is : September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
month = input('Insert a month: ')

if month == 'September' or 'October' or 'November':
    print('Autumn')
elif month == 'December' or 'January' or 'February':
    print('Winter')
elif month == 'March' or 'April' or 'May':
    print('Spring')
elif month == 'June' or 'July' or 'August':
    print('Summer')


# The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

fruit = input('Insert a fruit: ')

if fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(fruit)
    print(fruits)
