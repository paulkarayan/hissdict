"""
HissDict - a pure-Python Dictionary implementation
===========================================================
provides the same methods as the CPython dict, but with
a pure-Python implementation based on Collections' Abstract Base Classes

###use examples will go here###
"""

from collections import MutableMapping

class HissDict(MutableMapping):

    def __init__(self, *args, **kwargs):
        temp = dict(*args, **kwargs)
        self._keys = [None]*8
        self._values = [None]*8
        self._len = 0
        self._container_size = 8

        for key, value in temp.iteritems():
            self[key] = value   #calls __setitem__

    def create_index(self, key):
        hash_key = hash(key)
        index = hash_key % len(self._keys)
        return index

    def __setitem__(self, key, value):
        index = self.create_index(key)
        #increment to find an empty bucket or duplicate key
        while self._keys[index] is not None: #or self._keys[index] != key:
            index += 1

        self._keys[index] = key
        self._values[index] = value
        self._len += 1

    def __getitem__(self, key):
        index = self.create_index(key)
        while self._keys[index] is not None or self._keys[index] != key:
            index += 1
        return self._keys[index]

    def __delitem__(self, key):
        index = self.create_index(key)
        while self._keys[index] is not None or self._keys[index] != key:
            index += 1
        self._keys[index] = None
        self._values[index] = None
        self._len -= 1

    def __iter__(self):
        for key in self._keys:
            if key is not None:
                yield key

    def __len__(self):
        """Return the number of entries in the dictionary."""
        return self._len

    def __str__(self):
        """Return a String representation of the HissDict contents"""
        kvs = ["{key}: {value}".format(key=key, value=value) for key, value in zip(self._keys, self._values)]
        return ", ".join(kvs)
