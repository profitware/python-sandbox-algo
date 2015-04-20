# -*- coding: utf-8 -*-

__author__ = 'Sergey Sobko'


def flatten(in_list):
    """Flatten list.

    >>> flatten([])
    []

    >>> flatten([1, 2, 3])
    [1, 2, 3]

    >>> flatten(([[1], [2, 3]]))
    [1, 2, 3]

    >>> flatten([1, [[2], 3]])
    [1, 2, 3]

    """

    def flatten_generator(in_list_inner):
        for item in in_list_inner:
            try:
                for inner_item in flatten_generator(item):
                    yield inner_item
            except TypeError:
                yield item

    return list(flatten_generator(in_list_inner=in_list))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
