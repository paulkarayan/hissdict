"""
Decorator to count the number of function calls by a specific other function
see: http://stackoverflow.com/questions/1301735/counting-python-method-calls-within-another-method

Example usage:

@function_call_counter
def foo():
    return

def bar(y):
    foo()
    foo()

bar(1)
print foo.calls
"""

def function_call_counter(fn):
    def _counting(*args, **kwargs):
        _counting.calls += 1
        return fn(*args, **kwargs)
    _counting.calls = 0
    return _counting
