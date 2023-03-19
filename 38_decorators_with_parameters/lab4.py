def dec1(func):
    def wrapper():
        print("dec1")
        func()
        print("dec1 end")

    return wrapper


def dec2(func):
    def wrapper():
        print("dec2")
        func()
        print("dec2 end")

    return wrapper


@dec1
@dec2
def main():
    print("main")


if __name__ == '__main__':
    main()
