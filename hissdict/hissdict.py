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

from __future__ import division
from collections import MutableMapping
from copy import deepcopy

class HissDict(MutableMapping):

    def __init__(self, *args, **kwargs):
        temp = dict(*args, **kwargs)
        self._buckets = 3
        self._keys = [None]* (2 ** self._buckets)
        self._values = [None] * (2 ** self._buckets)
        #Fraction of buckets that are full before increasing allocation to 2^n+1
        self._upper_sparsity_value = 0.5
        #The lower end sparsity value is smaller to avoid expensive contractions with small numbers of deletes
        self._lower_sparsity_value = 0.2
        self._len = 0
        self._container_size = len(self._keys)
        #keep internal container utilization log for (possible) later tests
        self._expansion_log = list()

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
        self.check_appropriate_container_size(key, value)

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

        self.check_appropriate_container_size(key, value=None)

    def __iter__(self):
        for key in self._keys:
            if key is not None:
                yield key

    def __len__(self):
        """Return the number of entries in the dictionary."""
        return self._len

    def __str__(self):
        """Return a String representation of the HissDict contents"""
        kvs = ["{key}: {value}".format(key=key, value=self.__getitem__(key))    for key in self.__iter__()]
        return "{" + ", ".join(kvs) + "}"

    def check_appropriate_container_size(self, key, value):
        """Expands or Contracts the container size to optimize utilization"""
        self._container_utilization = self._len / self._container_size

        log_item_template = {
                "key": key,
                "value": value,
                "container_utilization":  self._container_utilization,
                "current_entries": self._len,
                "container_size": self._container_size,
            }

        if self._container_utilization >= self._upper_sparsity_value:
            #logging internal container utililization
            log_item = deepcopy(log_item_template)
            log_item["type"] = "expansion"
            self._expansion_log.append(log_item)
            self._buckets += 1
            self.alter_container_size()

        elif self._container_utilization < self._lower_sparsity_value and self._buckets > 3:
            log_item = deepcopy(log_item_template)
            log_item["type"] = "contraction"
            self._expansion_log.append(log_item)
            self._buckets -= 1
            self.alter_container_size()

        else:
            return

    def alter_container_size(self):
        #we could just append more None values, but this would
        #not distribute the items evenly (optional: could test if this matters...)

        #remember we can't just set this to temp vars, they'll be superficial!
        temp_keys = deepcopy(self._keys)
        temp_values = deepcopy(self._values)
        temp_len = deepcopy(self._len)

        self._keys = [None]* (2 ** self._buckets)
        self._values = [None] * (2 ** self._buckets)

        #update previous container size value
        self._container_size = len(self._keys)


        for key, value in zip(temp_keys, temp_values):
            if key != None:
                self.__setitem__(key, value)

        self._len = temp_len
