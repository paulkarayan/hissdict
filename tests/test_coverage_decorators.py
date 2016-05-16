# -*- coding: utf-8 -*-

from counting import function_call_counter


def test_func_counting():
    @function_call_counter
    def foo(x):
        return x

    def bar(x):
        foo(x)
        foo(x)

    bar(2)
    assert foo.calls == 2

if __name__ == '__main__':
    import nose
    nose.main()
