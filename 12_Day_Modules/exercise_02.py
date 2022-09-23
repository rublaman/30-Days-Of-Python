import random
import string

# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array(six hexadecimal numbers written after  # . Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).


def list_of_hexa_colors():
    random_number = random.randint(0, 16777215)
    hex_number = str(hex(random_number))
    hex_number = '#' + hex_number[2:]
    return hex_number


list_of_hexa_colors()

# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.


def list_of_rgb_colors():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return "rgb({},{},{})".format(red, green, blue)


list_of_rgb_colors()

# Write a function generate_colors which can generate any number of hexa or rgb colors.


def generate_colors(mode: string, num_colour: list):
    res = []
    if mode == "hexa":
        for _ in range(num_colour):
            res.append(list_of_hexa_colors())
    elif mode == "rgb":
        for _ in range(num_colour):
            res.append(list_of_rgb_colors())

    print(res)


generate_colors('hexa', 3)  # ['#a3e12f','#03ed55','#eb3d2b']
generate_colors('hexa', 1)  # ['#b334ef']
# ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80']
generate_colors('rgb', 3)
generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
