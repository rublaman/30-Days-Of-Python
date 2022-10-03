'''
What is the most frequent word in the following paragraph?

output:

    [
    (6, 'love'),
    (5, 'you'),
    (3, 'can'),
    (2, 'what'),
    (2, 'teaching'),
    (2, 'not'),
    (2, 'else'),
    (2, 'do'),
    (2, 'I'),
    (1, 'which'),
    (1, 'to'),
    (1, 'the'),
    (1, 'something'),
    (1, 'if'),
    (1, 'give'),
    (1, 'develop'),
    (1, 'capabilities'),
    (1, 'application'),
    (1, 'an'),
    (1, 'all'),
    (1, 'Python'),
    (1, 'If')
    ]
'''

import re
from collections import Counter
from turtle import distance

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

matches = re.findall(r'[A-Za-z]+', paragraph)
w_counter = Counter(matches)
print(w_counter)


paragrah_two = '''The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 
in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract 
these numbers from this whole text and find the distance between the two furthest 
particles.'''


points = re.findall(r'[-]\d+|\d+', paragrah_two)
point_int = [int(i) for i in points]
point_distance = point_int[-1] - point_int[0]
print(point_distance)


# points = ['-1', '2', '-4', '-3', '-1', '0', '4', '8']
# sorted_points = [-4, -3, -1, -1, 0, 2, 4, 8]
# distance = 8 - (-4)  # 12
