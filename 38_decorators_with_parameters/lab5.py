import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def wrapper():
        s = time.time()
        func()
        print(func.__name__, "total time", time.time() - s)

    return wrapper


@timeit
def sleep_10s():
    """sleep 10 seconds"""
    time.sleep(5)


if __name__ == '__main__':
   print("func", sleep_10s.__name__)
   print("doc", sleep_10s.__doc__)