The ``4-print_square`` module
============================

Using ``print_square``
---------------------

Importing function from the module:

    >>> print_square = __import__('4-print_square').print_square

Printing a square with a size of 5

    >>> print_square(5)
    #####
    #####
    #####
    #####
    #####

Passing 0 as the size of the square

    >>> print_square(0)

Passing a float number as the size of the square

    >>> print_square(1.0)
    Traceback (most recent call last):
    	      ...
    TypeError: size must be an integer

Passing a string as the size of the square

    >>> print_square('2')
    Traceback (most recent call last):
    	      ...
    TypeError: size must be an integer

Passing a negative number as the size of the square

    >>> print_square(-2)
    Traceback (most recent call last):
    	     ...
    ValueError: size must be >= 0

Passing None as the size of the square

    >>> print_square(None)
    Traceback (most recent call last):
    	      ...
    TypeError: size must be an integer

Missing argument

   >>> print_square()
   Traceback (most recent call last):
   	     ...
   TypeError: print_square() missing 1 required positional argument: 'size'
