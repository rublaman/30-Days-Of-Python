# Use for loop to iterate from 0 to 100 and print the sum of all numbers. The sum of all numbers is 5050.

from sre_constants import OPCODES


count = 0
for n in range(0, 101):
    count += n
else:
    print(count)

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds. The sum of all evens is 2550. And the sum of all odds is 2500.

evens = 0
odds = 0
for n in range(0, 101):
    if (n % 2 == 0):
        evens += n
    else:
        odds += n
else:
    print('Evens {} and {} odds'.format(evens, odds))
