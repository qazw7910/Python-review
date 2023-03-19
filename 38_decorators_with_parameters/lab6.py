class ClsDeco:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("before calling", self.func.__name__)
        self.func()
        print("after calling", self.func.__name__)


@ClsDeco
def say_hello():
    print("Hello!")


if __name__ == '__main__':
    say_hello()
