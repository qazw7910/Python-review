def sum(a, b):
    return a + b


def debug(func):
    print(f"receive:{func.__name__}")

    def wrapper(*args, **kwargs):
        print(f"proxy:{args}")
        print(f"proxy:{kwargs}")
        result = func(*args, **kwargs)
        print(func.__name__, "result", result)
    return wrapper


debug_sum = debug(sum)
debug_sum(1, 3)
