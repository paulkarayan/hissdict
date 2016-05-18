HissDict - a pure-Python Dictionary implementation
==================================================
HissDict is an Apache2 licensed dictionary implementation in
pure-Python, that uses [Collections' Abstract Base Classes](https://docs.python.org/3/library/collections.abc.html)
to model the CPython builtin dict. The major motivation is to illustrate performance differences between the two implementations.

## Use Example(s)
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

## Performance tests
Note that HissDict stopped responding on my local machine as the number of items increased, which you'll see by missing data points. So, some profiling and additional investigation is in order. 



## TODOs
* (optional) Count number of collisions at different sizes / sparsity constants
* (optional) Clean up some of the "todo" comments (by fixing the issues, obvi.)
* (optional) _check to test invariants
* (optional) setup for Pypi and add other niceties including:
    1. requirements.txt
    2. tox.ini
    3. Makefile
    4. setup.py
    5. TravisCI
