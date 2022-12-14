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

'''
DECORATING FUNCTIONS WITH ARGUMENTS
The problem is that the inner function wrapper_do_twice() does not take any arguments, 
but name="World" was passed to it. You could fix this by letting wrapper_do_twice() 
accept one argument, but then it would not work for the say_whee() function you created 
earlier.

The solution is to use *args and **kwargs in the inner wrapper function. Then it will 
accept an arbitrary number of positional and keyword arguments.
'''


@do_twice
def greet(name):
    print(f"Hello {name}")


greet('Ruben')

'''
RETURNING VALUES FROM DECORATED FUNCTIONS
What happens to the return value of decorated functions? Well, that's up to the decorator t
o decide.

>>> hi_adam = return_greeting("Adam")
Creating greeting
Creating greeting
>>> print(hi_adam)
None

Oops, your decorator ate the return value from the function. Because the do_twice_wrapper() 
doesn't explicitly return a value, the call return_greeting("Adam") ended up returning None.
To fix this, you need to make sure the wrapper function returns the return value of the 
decorated function. 

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice
    
The return value from the last execution of the function is returned:
>>> return_greeting("Adam")
Creating greeting
Creating greeting
'Hi Adam'
'''


@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


hi_ruben = return_greeting('Ruben')
print(hi_ruben)

'''
WHO ARE YOU, REALLY??
. Introspection is the ability of an object to know about its own attributes at runtime. For instance,
a function knows its own name and documentation. The introspection works for functions you define yourself 
as well. However, after being decorated, say_whee() has gotten very confused about its identity. It now 
reports being the wrapper_do_twice() inner function inside the do_twice() decorator. Although technically 
true, this is not very useful information.

To fix this, decorators should use the @functools.wraps decorator, which will preserve information about 
the original function.

import functools

def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice
'''

print(say_whee)
print(say_whee.__name__)
print(help(say_whee))
