"""
HissDict - a pure-Python Dictionary implementation
"""

from collections import MutableMapping

#sentinal
NONE = object()

class HissDict(MutableMapping):

    def __init__(self, *args, **kwargs):
        temp = dict(*args, **kwargs)
        self._keys = [None]*8
        self._values = [None]*8

        for key, value in temp.iteritems():
            self[key] = value   #calls __setitem__

    def __setitem__(self, key, value):
        hash_key = hash(key)
        index = hash_key % len(self._keys)
        while self._keys[index] is not NONE or self._keys[index] != key:
            index += 1
        self._keys[index] = key
        self._values[index] = value

    def __getitem__(self, key):
        hash_key = hash(key)
        index = hash_key % len(self._keys)
        while self._keys[index] is not NONE or self._keys[index] != key:
            index += 1
        return self._keys[index]

    def __delitem__(self, key):
        hash_key = hash(key)
        index = hash_key % len(self._keys)
        while self._keys[index] is not NONE or self._keys[index] != key:
            index += 1
        self._keys[index] = NONE
        self._values[index] = NONE

    def __iter__(self):
        for key in self._keys:
            if key is not NONE:
                yield key

    def __len__(self):
        return sum(1 for key in self)
