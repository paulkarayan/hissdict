"""
Decorator to count the number of function calls by a specific other function
see: http://stackoverflow.com/questions/1301735/counting-python-method-calls-within-another-method
"""

def function_call_counter(other):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            other.called= 0
            try:
                return fn(*args, **kwargs)
            finally:
                print '%s was called %i times' % (other.__name__, other.called)
        wrapper.__name__= fn.__name__
        return wrapper
    return decorator
