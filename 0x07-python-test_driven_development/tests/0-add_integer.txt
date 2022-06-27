The ``0-add_integer`` module
============================

Using ``add_integer``
---------------------

Importing function from the module:
    >>> add_integer = __import__('0-add_integer').add_integer

Adding 1 and 2
    >>> add_integer(1, 2)
    3

Subtracting 100 and 2
    >>> add_integer(100, -2)
    98

Adding 2.1 and 98
    >>> add_integer(2.1)
    100

Subtracting 100.3 and 2
	    >>> add_integer(100.3, -2)
	    98

Adding an integer number and a string
    >>> add_integer(4, "School")
    Traceback (most recent call last):
	      ...
    TypeError: b must be an integer

Passing None
    >>> add_integer(None)
    Traceback (most recent call last):
	      ...
    TypeError: a must be an integer

Adding a letter and a number
    >>> add_integer('1', 1)
    Traceback (most recent call last):
              ...
    TypeError: a must be an integer

Adding two letters
    >>> add_integer('2', '1')
    Traceback (most recent call last):
              ...
    TypeError: a must be an integer

Adding a tuple
    >>> add_integer((1, 1))
    Traceback (most recent call last):
              ...
    TypeError: a must be an integer

Adding a number and a list
    >>> add_integer(123, [])
    Traceback (most recent call last):
	      ...
    TypeError: b must be an integer

Passing a string
    >>> add_integer("Hello")
    Traceback (most recent call last):
	      ...
    TypeError: a must be an integer

Adding two float numbers
    >>> add_integer(2.9, 2.9)
    4

Subtracting 98 and 1
    >>> add_integer(-1)
    97

Case Overflow:

    >>> add_integer(float('inf'), 0)
    Traceback (most recent call last):
    	      ...
    OverflowError: cannot convert float infinity to integer

Case Overflow 2:

    >>> add_integer(float('inf'), float('-inf'))
    Traceback (most recent call last):
    	      ...
    OverflowError: cannot convert float infinity to integer

Case NaN:

    >>> add_integer(0, float('nan'))
    Traceback (most recent call last):
    	      ...
    ValueError: cannot convert float NaN to integer
