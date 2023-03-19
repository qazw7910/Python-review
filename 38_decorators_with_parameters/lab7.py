from functools import wraps


def retry(max=1):
    @wraps
    class Wrapper:
        def __init__(self, func):
            self.func = func

        def __call__(self):
            retried = 0
            while retried < max:
                try:
                    self.func()
                except Exception:
                    retried += 1
                    print(f"Failed. Going to try again (' {retried} ')")
                else:
                    break

    return Wrapper


@retry(max=3)
def get_stock_price():
    raise ValueError


if __name__ == '__main__':
    get_stock_price()
    print(get_stock_price.__name__)
