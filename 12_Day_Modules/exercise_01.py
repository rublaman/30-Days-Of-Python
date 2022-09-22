# Write a function which generates a six digit/character random_user_id.

from random import random, shuffle, randint
import string


def random_user_id(n_char: int):
    user_id = ""
    characters = list(string.ascii_letters + string.digits)
    shuffle(characters)
    for _ in range(n_char):
        user_id += characters[randint(0, len(characters) - 1)]
    return user_id


print(random_user_id(6))
'1ee33d'
# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.


def user_id_gen_by_user(num_ids: int, lenght_id: int):
    list = []
    for _ in range(num_ids):
        list.append(random_user_id(lenght_id))

    res = ""
    for id in list:
        res += "{}\n".format(id)

    return res


print(user_id_gen_by_user(5, 5))  # user input: 5 5
# output:
# kcsy2
# SMFYb
# bWmeq
# ZXOYh
# 2Rgxf

print(user_id_gen_by_user(5, 16))  # 5 16
# # 1GCSgPLMaBAVQZ26
# # YD7eFwNQKNs7qXaT
# # ycArC5yrRupyG00S
# # UbGxOFI7UXSWAyKN
# # dIV0SSUTgAdKwStr

# Write a function named rgb_color_gen. It will generate rgb colors(3 values ranging from 0 to 255 each).


def rgb_color_gen():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    return "rgb({},{},{})".format(red, green, blue)


print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form
