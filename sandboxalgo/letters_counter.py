# -*- coding: utf-8 -*-

__author__ = 'Sergey Sobko'


def count_letters(letters_in):
    """Count repeating letters using reduction.

    >>> count_letters('aaaaabbbbccccccaaaaaaa')
    '5a4b6c7a'

    >>> count_letters('xxxxyycdd')
    '4x2y1c2d'

    >>> count_letters('')
    ''
    """

    def reducer(accumulator, new_letter):
        full_string, last_letter, count = accumulator

        if last_letter != new_letter:
            if last_letter:
                full_string += '{}{}'.format(count, last_letter)

            count = 1
            last_letter = new_letter

        else:
            count += 1

        return full_string, last_letter, count

    full_string, last_letter, count = reduce(reducer, letters_in, ('', None, 0))

    return '{}{}{}'.format(full_string, count, last_letter) if full_string else ''


if __name__ == '__main__':
    import doctest
    doctest.testmod()
