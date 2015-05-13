#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Sergey Sobko'
__email__ = 'S.Sobko@profitware.ru'
__copyright__ = 'Copyright 2015, The Profitware Group'


RUSSIAN_ALPHA = u'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
TOPIC_COUNTS = [13, 10 + 4 + 6 + 6, 14, 5, 15, 18, 10, 10, 14, 18]


def get_question_number(surname, topic_number):
    surname_length = len(surname)
    letter1, letter2 = \
        surname[((topic_number % surname_length) - 1) % surname_length], \
        surname[((topic_number % surname_length) + 2) % surname_length]

    topic_count = TOPIC_COUNTS[topic_number - 1]

    return (RUSSIAN_ALPHA.index(letter1) + 1) % topic_count, \
           (RUSSIAN_ALPHA.index(letter2) + 1) % topic_count


if __name__ == '__main__':
    SURNAME = u'Собко'.lower()

    for i in range(1, len(TOPIC_COUNTS) + 1):
        print i, get_question_number(SURNAME, i)
