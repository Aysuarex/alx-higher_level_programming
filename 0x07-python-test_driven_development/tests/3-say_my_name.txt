The ``3-say_my_name`` module
============================

Using ``say_my_name``
---------------------

Importing function from the module:

    >>> say_my_name = __import__('3-say_my_name').say_my_name

Passing first_name and last_name correctly

    >>> say_my_name("Betty", "Holberton")
    My name is Betty Holberton

Passing first_name and last_name correctly 2

    >>> say_my_name("Luis")
    My name is Luis 

Passing None as the last_name

    >>> say_my_name("John", None)
    Traceback (most recent call last):
    	      ...
    TypeError: last_name must be a string

Passing None as the first_name

    >>> say_my_name(None)
    Traceback (most recent call last):
    	      ...
    TypeError: first_name must be a string

Passing a number as the first_name

    >>> say_my_name(1)
    Traceback (most recent call last):
    	      ...
    TypeError: first_name must be a string

Passing a number as the last_name

    >>> say_my_name("Betty", 0)
    Traceback (most recent call last):
    	      ...
    TypeError: last_name must be a string

Missing two arguments

    >>> say_my_name()
    Traceback (most recent call last):
    	      ...
    TypeError: say_my_name() missing 1 required positional argument: 'first_name'
