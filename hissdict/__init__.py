# -*- coding: utf-8 -*-

"""
HissDict - a pure-Python Dictionary implementation
==================================================
HissDict is an Apache2 licensed dictionary implementation in
pure-Python, that uses Collections' Abstract Base Classes to model
the CPython builtin dict.

See: https://docs.python.org/3/library/collections.abc.html

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

Inspired by Grant "Sir Hiss" Jenks and his excellent SortedContainers project.

:copyright: (c) 2016 by Grant Jenks, Paul Karayan.
:license: Apache 2.0, see LICENSE for more details.
"""


__title__ = 'hissdict'
__version__ = '0.0.1'
__author__ = 'Paul Karayan, Grant Jenks'
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2016 Paul Karayan, Grant Jenks'

from hissdict import HissDict

__all__ = ['HissDict',]
