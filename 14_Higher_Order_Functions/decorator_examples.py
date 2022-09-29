'''
SIMPLE DECORATORS
Decorators allow us to wrap another function in order to extend the 
behaviour of the wrapped function, without permanently modifying it.

Put simply: decorators wrap a function, modifying its behavior.
'''


from decorators import do_twice
from datetime import datetime


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


def say_whee():
    print("Whee!")


say_whee = my_decorator(say_whee)
print(say_whee)

# EXAMPLE 2


def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper


def say_whee():
    print("Whee!")


say_whee = not_during_the_night(say_whee)
print(say_whee)

'''
SYNTACTIC SUGAR
Python allows you to use decorators in a simpler way with the @ symbol,
sometimes called the “pie” syntax. 

'''


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


@my_decorator
def say_whee():
    print("Whee!")


# So, @my_decorator is just an easier way of saying say_whee = my_decorator(say_whee). It’s how you apply a decorator to a function.
say_whee()


'''
REUSING DECORATORS
Recall that a decorator is just a regular Python function. All the usual tools 
for easy reusability are available. We can move the decorator to another .py file
and then import it in other file.
'''


@do_twice
def say_whee():
    print("Whee!")


say_whee()
