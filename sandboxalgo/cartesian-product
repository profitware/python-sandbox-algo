# -*- coding: utf-8 -*-

__author__ = 'Sergey Sobko'
__email__ = 'S.Sobko@profitware.ru'
__copyright__ = 'Copyright 2016, The Profitware Group'


def cartesian_product(*iterables):
    def inner_product(master, slave):
        if not master:
            for a in slave:
                yield a

        for a in master:
            for b in slave:
                yield (a if isinstance(a, list) else [a]) + [b]

    return reduce(
        inner_product,
        map(list, iterables)
    )


if __name__ == '__main__':
    for new_list in cartesian_product([1, 2, 3], [4, 5, 6], ['a', 'b', 'c', 'd']):
        print new_list
