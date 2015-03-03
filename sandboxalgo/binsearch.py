# -*- coding: utf-8 -*-

__author__ = 'Sergey Sobko'


KEY_NOT_FOUND = -1


def midpoint(imin, imax):
    """Returns middle point

    >>> midpoint(0, 0)
    0

    >>> midpoint(0, 1)
    0

    >>> midpoint(0, 2)
    1

    >>> midpoint(1, 1)
    1

    >>> midpoint(1, 2)
    1

    >>> midpoint(1, 5)
    3

    """

    middle_point = (int(imin) + int(imax)) / 2
    return middle_point


def binary_search(search_list, key):
    """Binary search algorithm

    >>> binary_search([], 1) == KEY_NOT_FOUND
    True

    >>> binary_search([1, 3, 4, 6, 8, 9, 11], 4)
    2

    >>> binary_search([1, 2, 3, 4, 6, 8, 9, 11], 4)
    3

    >>> binary_search([1, 2, 3, 4, 6, 8, 9, 11], 1)
    0

    >>> binary_search([1, 2, 3, 4, 6, 8, 9, 11], 11)
    7

    >>> binary_search([1, 2, 3, 4, 8, 9, 11], 11)
    6

    >>> binary_search([1, 2, 3], 4) == KEY_NOT_FOUND
    True

    >>> binary_search([-1, 2, 4], 0) == KEY_NOT_FOUND
    True


    """

    if not search_list:
        return KEY_NOT_FOUND

    list_last_index = len(search_list) - 1

    if search_list[list_last_index] == key:
        return list_last_index

    def _binary_search(imin, imax, previous_index=-1):
        current_index = midpoint(imin, imax)

        if previous_index == current_index:
            return KEY_NOT_FOUND

        if search_list[current_index] == key:
            return current_index

        if key < search_list[current_index]:
            return _binary_search(imin, current_index, current_index)
        else:
            return _binary_search(current_index, imax, current_index)

    return _binary_search(0, list_last_index)


def binary_search_func(function, key, eps, imin, imax):
    """Binary search for monotonically increasing function.

    """
    # FIXME: Doctests

    def _mid_point(xmin, xmax):
        return (xmin + xmax) / 2

    xmin, xmax = imin, imax
    previous_x = None

    while True:
        current_x = _mid_point(xmin, xmax)

        current_value = function(current_x)

        if abs(current_value - key) < eps:
            return current_x

        if previous_x is not None:
            if abs(current_x - previous_x) < eps:
                break

        if key < current_value:
            xmax = current_x
        else:
            xmin = current_x

        previous_x = current_x

    return None


if __name__ == '__main__':
    import doctest
    doctest.testmod()
