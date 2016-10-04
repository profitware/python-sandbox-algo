# -*- coding: utf-8 -*-

__author__ = 'Sergey Sobko'


def lines_with_equal_column_data(lines, column):
    """Return lines containing equal data in same column.

    >>> lines_with_equal_column_data([], 0)
    []

    >>> lines_with_equal_column_data([(2, 3), (5, 2), (9, 3)], 0)
    []

    >>> lines_with_equal_column_data([(2, 3), (5, 2), (9, 3)], 1)
    [(2, 3), (9, 3)]

    >>> lines_with_equal_column_data([(2, 3), (5, 2), (2, 3)], 0)
    [(2, 3), (2, 3)]
    """

    def lines_with_equal_column_data_inner():
        lines_data_dict = dict()

        for i, line in enumerate(lines):
            lines_data_dict.setdefault(line[column], []).append(line)

        for values in lines_data_dict.itervalues():
            if len(values) > 1:
                for value in values:
                    yield value

    return list(lines_with_equal_column_data_inner())


if __name__ == '__main__':
    import doctest
    doctest.testmod()
