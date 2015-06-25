#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Sergey Sobko'
__email__ = 'S.Sobko@profitware.ru'
__copyright__ = 'Copyright 2015, The Profitware Group'

import dis
import random
import timeit

random.seed()
GLOBAL_RANDOM_LIST = [random.randint(0, 100) for _ in xrange(100)]


def my_generator(count):
    random_list = GLOBAL_RANDOM_LIST
    current_value = 1

    for i in xrange(1, count):
        if i % 2 == 0:
            current_value *= random_list[i]
        else:
            current_value += random_list[i]
        
        yield current_value

if __name__ == '__main__':

    def append_function(x=100):
        return_list = []
        for value in my_generator(x):
            return_list.append(value)

        return return_list

    list_comprehension_function = lambda x=100: [x for x in my_generator(x)]
    list_function = lambda x=100: list(my_generator(x))

    dis.dis(append_function)
    print timeit.timeit(stmt=append_function, number=1000)

    dis.dis(list_comprehension_function)
    print timeit.timeit(stmt=list_comprehension_function, number=1000)

    dis.dis(list_function)
    print timeit.timeit(stmt=list_function, number=1000)

