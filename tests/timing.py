"""
Decorator to time function runtimes
Example usage:

@timing
def create_dict(input_data):
    ex_dict = dict((key, value) for key, value in input_data)
    return ex_dict
"""

from functools import wraps
from time import time

#@wraps to preserve original function metadata. see:
# https://docs.python.org/2/library/functools.html

def timing(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        # print 'func:%r args:[%r, %r] took: %2.4f sec' % \
        #   (func.__name__, args, kwargs, end-start)
        return result, func.__name__, end-start
    return wrap
