# -*- coding: utf-8 -*-

__author__ = 'Sergey Sobko'


class HashSet(object):
    _set_dict = None

    def __init__(self):
        self._set_dict = dict()

    def add(self, key, value):
        self._set_dict[hash(key)] = value

    def get(self, key):
        return self._set_dict.get(hash(key))

    def __repr__(self):
        return self._set_dict


class LexNode(object):
    letter = None
    data = None
    next_letters = None

    def __init__(self, letter):
        self.letter = letter
        self.next_letters = list()

class TreeSet(object):
    root_letter = None

    def __init__(self):
        self.root_letter = LexNode(None)

    def add(self, key, value):

        assert isinstance(key, basestring)

        current_node = self.root_letter
        for letter in key:
            pass
            # FIXME: Step into next letter's LexNode