#a decorator to measure the performance of the function fn
from functools import wraps
def time_decorator(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        from time import perf_counter
        counter = perf_counter()
        fn(*args,**kwargs)
        counter = perf_counter() - counter
        return counter
    return wrapper
    