The ``2-matrix_divided`` module
============================

Using ``matrix_divided``
---------------------

Importing function from the module:

    >>> matrix_divided = __import__('2-matrix_divided').matrix_divided

Dividing a matrix by 3:

    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

Dividing a matrix by 0:

    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 0)
    Traceback (most recent call last):
    	      ...
    ZeroDivisionError: division by zero

Dividing a matrix by a float number:

    >>> matrix_divided([[10, 20, 30], [1.33, 3.74, 6.89], [-8, -9.71, 0]], 5.3)
    [[1.89, 3.77, 5.66], [0.25, 0.71, 1.3], [-1.51, -1.83, 0.0]]

Passing an empty matrix:

    >>> matrix_divided([], 10)
    Traceback (most recent call last):
    	      ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

Passing a tuple as an argument:

    >>> matrix_divided((3, 6, 9), 3)
    Traceback (most recent call last):
    	      ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

Dividing a matrix which its rows don't have the same size:

    >>> matrix_divided([[22, 34], [2.78, 7.1, -10, 2], [-8]], 3)
    Traceback (most recent call last):
    	      ...
    TypeError: Each row of the matrix must have the same size

Dividing a matrix which its rows don't have the same size 2:

    >>> matrix_divided([[2, 4], [6.8], [10, 12]], 12)
    Traceback (most recent call last):
    	      ...
    TypeError: Each row of the matrix must have the same size

Dividing a matrix which its elements aren't integer/float numbers:

    >>> matrix_divided([["Hello", "World"], ["Hello", "Holberton"]], 10)
    Traceback (most recent call last):
     	       ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

Dividing a matrix which its elements aren't integer/float numbers 2:

    >>> matrix_divided([["1"], ["2", "3"], ["5", "6", "7"]], 10)
    Traceback (most recent call last):
    	      ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

Dividing a matrix which some of its elements aren't integer/float numbers:

    >>> matrix_divided([[2.7, 4], ['6', 8.4], [10.1, '12'], [5.3, '10.2', 15.8]], 5)
    Traceback (most recent call last):
    	      ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

Passing a matrix which one of its elements is an empty list:

    >>> matrix_divided([[2.1, 5.8], [], [10, -3]], 8)
    Traceback (most recent call last):
    	      ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

Passing a matrix which one of its elements is a tuple:

    >>> matrix_divided([[1, -1], (2, -2), [3, -3]], 1)
    Traceback (most recent call last):
    	      ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

Passing div as a list

    >>> matrix_divided([[5.7, 8.1], [7.7, 4.9]], [2])
    Traceback (most recent call last):
    	      ...
    TypeError: div must be a number

Passing div as a string

    >>> matrix_divided([[10, 50], [30, 20]], "10")
    Traceback (most recent call last):
    	      ...
    TypeError: div must be a number

Dividing a matrix which has positive and negative integer/float numbers

    >>> matrix_divided([[-1, 3.1, 0], [78, -103.7, 54]], 9.2)
    [[-0.11, 0.34, 0.0], [8.48, -11.27, 5.87]]
