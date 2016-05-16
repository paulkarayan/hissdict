"""
HissDict - a pure-Python Dictionary implementation
===========================================================
provides the same methods as the CPython dict, but with
a pure-Python implementation based on Collections' Abstract Base Classes

Use Example(s):
>>> from hissdict import HissDict
>>> hd = HissDict([('New York', 'Albany'), ('California', 'Sacramento')])
>>> california_capital = hd.get('California')
>>> print california_capital
Sacramento
>>>
>>> del hd["New York"]
>>> hd["North Carolina"] = "Raleigh"
>>> print hd.__str__()
{New York: Albany, California: Sacramento}
>>>
>>> for state in iter(hd):
...     print state
...
California
North Carolina
"""

from collections import MutableMapping

class HissDict(MutableMapping):

    def __init__(self, *args, **kwargs):
        temp = dict(*args, **kwargs)
        self._keys = [None]*8
        self._values = [None]*8
        #Fraction of buckets that are full before increasing allocation to 2^n+1
        self._sparsity_value = 0.5
        self._len = 0
        self._container_size = len(self._keys)

        for key, value in temp.iteritems():
            self[key] = value   #calls __setitem__

    def create_index(self, key):
        hash_key = hash(key)
        index = hash_key % self._container_size
        #increment to find an empty bucket or duplicate key
        while self._keys[index] is not None and self._keys[index] != key:
            index = (index + 1) % self._container_size
        return index

    def __setitem__(self, key, value):
        index = self.create_index(key)
        self._keys[index] = key
        self._values[index] = value
        self._len += 1

    def __getitem__(self, key):
        index = self.create_index(key)
        return self._values[index]

    def __delitem__(self, key):
        index = self.create_index(key)
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
        kvs = ["{key}: {value}".format(key=key, value=value) for key, value in zip(self._keys, self._values) if key != None]
        return "{" + ", ".join(kvs) + "}"

