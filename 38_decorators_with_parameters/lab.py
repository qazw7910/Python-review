import functools


def main():
    print(example())
    print(example.__doc__)
    print(example.__name__)
    a =  A(1,2)

#-------use @functools.cache--------
    a = A(1, 2)
    print(a.plus())
    print(a.plus())#do not repeat call "hi"


class A:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    @functools.cache
    def plus(self):
        print("hi")
        return self.val1 + self.val2


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Calling decorated function')
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def example():
    """Docstring"""
    print('Called example function')


if __name__ == '__main__':
    main()
