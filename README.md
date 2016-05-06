HissDict - a pure-Python Dictionary implementation
==================================================
HissDict is an Apache2 licensed dictionary implementation in
pure-Python, that uses [Collections' Abstract Base Classes](https://docs.python.org/3/library/collections.abc.html)
to model the CPython builtin dict. The major motivation is to illustrate performance differences between the two implementations.

## Use Example(s):
```
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
```

Inspired by Grant "Sir Hiss" Jenks (@grantjenks) and his excellent [SortedContainers](http://www.grantjenks.com/docs/sortedcontainers/)
project.

## TODOs
* If mapping gets too "full" remap to larger keys and values list.
* If mapping gets too "sparse" remap to smaller keys and values list.
* Performance testing - benchmarking against CPython dict implementation
* (optional) _check to test invariants
* (optional) setup for Pypi and add other niceties including:
    1. requirements.txt
    2. tox.ini
    3. Makefile
    4. setup.py
    5. TravisCI
