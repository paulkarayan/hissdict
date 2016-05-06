# -*- coding: utf-8 -*-

from nose.tools import raises
from sys import hexversion
from context import hissdict
from hissdict import HissDict

if hexversion < 0x03000000:
    range = xrange

def test_init():
    temp = HissDict()

def test_init_args():
    temp = HissDict([('a', 1), ('b', 2)])
    assert len(temp) == 2
    assert temp['a'] == 1
    assert temp['b'] == 2

def test_init_kwargs():
    temp = HissDict(a=1, b=2)
    assert len(temp) == 2
    assert temp['a'] == 1
    assert temp['b'] == 2

if __name__ == '__main__':
    import nose
    nose.main()
