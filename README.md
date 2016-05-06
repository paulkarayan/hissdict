HissDict - a pure-Python Dictionary implementation
==================================================
HissDict is an Apache2 licensed dictionary implementation in
pure-Python, that uses [Collections' Abstract Base Classes](https://docs.python.org/3/library/collections.abc.html)
to model the CPython builtin dict. The major motivation is to illustrate performance differences between the two implementations.

-> use example goes here <-

Inspired by Grant "Sir Hiss" Jenks (@grantjenks) and his excellent [SortedContainers](http://www.grantjenks.com/docs/sortedcontainers/)
project.

TODO
=================================================
0. Write tests for existing methods
1. Add _len attribute to track length as we add key, value pairs.
2. Handle IndexError while iterating to wrap-around. (use modulo)
3. If mapping gets too "full" remap to larger keys and values list.
4. If mapping gets too "sparse" remap to smaller keys and values list.
5. Performance testing - comparison against CPython dict implementation
6. Create use example for readme, init, and sample.py
7. _check to test invariants
8.(optional) setup for Pypi and add other niceties including:
    a. requirements.txt
    b. tox.ini
    c. Makefile
    d. setup.py
    e. TravisCI
