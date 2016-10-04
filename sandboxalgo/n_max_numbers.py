# -*- coding: utf-8 -*-

__author__ = 'Sergey Sobko'

from bisect import insort_left


def n_max_numbers(in_iter, n=2):
    """Get N maximal numbers from iter.

    >>> n_max_numbers([])
    []

    >>> n_max_numbers([1, 2, 3])
    [2, 3]

    >>> n_max_numbers([4, 2, 3])
    [3, 4]

    >>> n_max_numbers([1, 2, -1, 0], 3)
    [0, 1, 2]

    """

    max_numbers = list()

    for number in in_iter:
        insort_left(max_numbers, number)
        max_numbers = max_numbers[-n:]

    return max_numbers


if __name__ == '__main__':
    import doctest
    doctest.testmod()
