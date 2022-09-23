# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

import random


def shuffle_list(params: list):
    random.shuffle(params)
    return params


print(shuffle_list([1, "Hola", 3, 4, 5, 6, 7]))


# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def random_array():
    res = []
    for _ in range(7):
        random_number = random.randint(0, 9)
        while (res.count(random_number) != 0):
            random_number = random.randint(0, 9)
        res.append(random_number)
    print(res)


random_array()
