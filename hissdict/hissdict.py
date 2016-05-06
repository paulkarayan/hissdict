"""
HissDict - a pure-Python Dictionary implementation
===========================================================
provides the same methods as the CPython dict, but with
a pure-Python implementation based on Collections' Abstract Base Classes

###use examples will go here###
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
            print key, value
            self[key] = value   #calls __setitem__

    def __setitem__(self, key, value):
        hash_key = hash(key)
        index = hash_key % len(self._keys)
        print index, hash_key, key, value, "<---"
        print self._keys, self._values
        print self._keys[index] is not None
        print self._keys[index] != key

        #increment to find an empty bucket (or duplicate key <--- need to add)
        while self._keys[index] is not None: # or self._keys[index] != key:
            index += 1

        self._keys[index] = key
        self._values[index] = value

    def __getitem__(self, key):
        hash_key = hash(key)
        index = hash_key % len(self._keys)
        while self._keys[index] is not None or self._keys[index] != key:
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

    #string representation of the HissDict contents
    def __str__(self):
        kvs = ["{key}: {value}".format(key=key, value=value) for key, value in zip(self._keys, self._values)]
        return kvs



hd = HissDict((e, i) for i, e in enumerate('abc'))
print hd.__str__()
