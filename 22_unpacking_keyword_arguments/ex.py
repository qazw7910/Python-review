def name(**kwargs):
    print(kwargs)


# name(name='bob', age=25)
# name(**{'name': 'bob', 'age': 25})


# ----------------------------------------------------------------

def named(**kwargs):
    print(kwargs)


def print_nicely(**kwargs):
    named(**kwargs)
    for key, val in kwargs.items():
        print(f'{key} : {val}')


print_nicely(name='bob', age=25)


# ----------------------------------------------------------------

def myfunction(**kwargs):
    print(kwargs)


myfunction(**"Bob")  # Error, must be mapping
myfunction(**None)  # Error