import time


def timeit(func):
    def wrapper():
        s = time.time()
        func()
        print(func.__name__, "total time", time.time() - s)

    return wrapper

@timeit
def sleep_10s():
    time.sleep(10)

if __name__ == '__main__':
    sleep_10s()