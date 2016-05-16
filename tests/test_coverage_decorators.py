# -*- coding: utf-8 -*-
from context import counting
from counting import function_call_counter

@function_call_counter()
def foo():
    return
def test_init():
    temp = HissDict()
    assert temp._container_size == 8



if __name__ == '__main__':
    import nose
    nose.main()
