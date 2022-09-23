#!/usr/bin/python3
""" finds a peak in a list of unsorted integers. """


def find_peak2(numbers, size, start, end):
    middle = int(start + (end - start) / 2)

    if ((middle is 0 or numbers[middle - 1] <= numbers[middle]) and
       (middle == size - 1 or numbers[middle + 1] <= numbers[middle])):
        return numbers[middle]
    elif (middle > 0 and numbers[middle - 1] > numbers[middle]):
        return find_peak2(numbers, size, start, (middle - 1))
    else:
        return find_peak2(numbers, size, middle + 1, end)


def find_peak(list_of_integers):
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 2:
        return (list_of_integers[0] if list_of_integers[0] >
                list_of_integers[1] else list_of_integers[1])
    return (find_peak2(list_of_integers, len(list_of_integers), 0,
            len(list_of_integers) - 1))
