# -*- coding: utf-8 -*-

from context import hissdict
from hissdict import HissDict
import string

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
    mapping = [(val, pos) for pos, val in enumerate(string.ascii_lowercase)]
    temp = HissDict(mapping)
    for key in temp.__iter__():
        if key not in ['a','b','c']:
            del temp[key]
    assert temp.__len__() == 3

def test_getitem():
    mapping = [(val, pos) for pos, val in enumerate(string.ascii_lowercase)]
    temp = HissDict(mapping)
    assert all((temp[val] == pos) for pos, val in enumerate(string.ascii_lowercase))

def test_len():
    temp = HissDict([('a', 1), ('b', 2)])
    assert temp.__len__() == 2
    temp['c'] = 3
    assert temp.__len__() == 3
    del temp['a']
    assert temp.__len__() == 2

def test_iter():
    mapping = [(val, pos) for pos, val in enumerate(string.ascii_lowercase)]
    temp = HissDict(mapping)
    assert [key in string.ascii_lowercase for key in temp._keys if key != None]

def test_str():
    mapping = [(val, pos) for pos, val in enumerate(string.ascii_lowercase)]
    temp = HissDict(mapping)
    assert isinstance(temp.__str__(), str)

def test_create_index():
    temp = HissDict([('a', 1)])
    assert temp.create_index('a') <= temp._len

# #test removed - not sure if there is a better way to test this now
# #that the HissDict expands?
# def test_index_wraparound():
#     #use a 8 item input to max out size of dictionary.
#     #it is very unlikely that we will not have had to wrap around
#     #to fit everything.
#     #todo: is there a better way to ensure we had a wrap around event?
#     temp = HissDict((val, pos) for pos, val in enumerate('abcefghi'))
#     assert None not in temp._keys

#Before feature implementation, HissDict stalls even with: @timed(.5)
def test_container_expansion():
    mapping = [(val, pos) for pos, val in enumerate(string.ascii_lowercase)]
    temp = HissDict(mapping)
    #should have 26 items in the dict
    assert temp.__len__() == 26, (temp._expansion_log, temp.__len__())
    #if expansion happened, the container size shouldn't be initial value
    assert temp._container_size != 8
    #if expansion happened, it should be logged (thus log not empty)
    assert temp._expansion_log
    #should log three expansions (8, 16, 32) to handle 26 keys at 50% util
    assert len(temp._expansion_log) == 3, (temp._expansion_log, len(temp._expansion_log))

def test_container_contraction():
    mapping = [(val, pos) for pos, val in enumerate(string.ascii_lowercase)]
    temp = HissDict(mapping)

    #delete down to just three items
    for key in temp.__iter__():
        if key not in ['a','b','c']:
            del temp[key]
    assert temp._container_size == 16

    del temp['a']
    del temp['b']
    #bottoms out at 8
    assert temp._container_size == 8



if __name__ == '__main__':
    import nose
    nose.main()
