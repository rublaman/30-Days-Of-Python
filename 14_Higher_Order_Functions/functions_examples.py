'''
FIST-CLASS OBJECTS
In Python, functions are first-class objects. This means that functions can 
be passed around and used as arguments, just like any other object (string, 
int, float, list, and so on).
'''


def say_hello(name):
    return f"Hello {name}"


def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"


def greet_bob(greeter_func):
    return greeter_func("Bob")


print(greet_bob(say_hello))

'''
INNER FUNCTIONS
It's possible to define functions inside other functions. Such functions are 
called inner functions. 

Note that the order in which the inner functions are defined does not matter. 
Like with any other functions, the printing only happens when the inner 
functions are executed.
'''


def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()


parent()

'''
RETURNING FUNCTIONS FROM FUNCTIONS

Python also allows you to use functions as return values. 


Note that you are returning without the parentheses. Recall that this means 
that you are returning a reference to the function first_child. In contrast 
with parentheses refers to the result of evaluating the function.
'''


def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child


first = parent(1)

print(first)
print(first())
