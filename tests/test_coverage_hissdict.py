# -*- coding: utf-8 -*-

from sys import hexversion
from context import hissdict
from hissdict import HissDict

if hexversion < 0x03000000:
    range = xrange

def test_init():
    temp = HissDict()
    assert temp._container_size == 8

#implicitly tests setitem
def test_init_args():
    temp = HissDict([('a', 1), ('b', 2)])
    assert temp['a'] == 1
    assert temp['b'] == 2

def test_init_kwargs():
    temp = HissDict(a=1, b=2)
    assert temp['a'] == 1
    assert temp['b'] == 2

def test_delitem():
    mapping = [(val, pos) for pos, val in enumerate('abc')]
    temp = HissDict(mapping)
    del temp['a']
    assert temp.__len__() == 3

def test_getitem():
    mapping = [(val, pos) for pos, val in enumerate('abc')]
    temp = HissDict(mapping)
    assert all((temp[val] == pos) for pos, val in enumerate('abc'))

def test_len():
    temp = HissDict([('a', 1), ('b', 2)])
    assert temp.__len__() == 2
    temp['c'] = 3
    assert temp.__len__() == 3
    ##remove until del works
    #del temp['a']
    #assert temp.__len__() == 2

def test_iter():
    mapping = [(val, pos) for pos, val in enumerate('abc')]
    temp = HissDict(mapping)
    assert [key in 'abc' for key in temp._keys if key != None]

def test_str():
    mapping = [(val, pos) for pos, val in enumerate('abc')]
    temp = HissDict(mapping)
    assert isinstance(temp.__str__(), str)
    ##todo: better way to assert the contents are there without using a hardcoded string? esp. since order preservation is not guaranteed

def test_create_index():
    temp = HissDict([('a', 1)])
    assert temp.create_index('a') <= temp._len

if __name__ == '__main__':
    import nose
    nose.main()
