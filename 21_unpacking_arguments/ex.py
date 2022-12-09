from certifi.__main__ import args


def multiply1(*args):
    print(args)
    total = 1
    for arg in args:
        total *= arg

    return total


# print(multiply(3, 5))
# print(multiply(-1))


def add(x, y):
    return x + y


# nums = [3, 5]
# print(add(nums[0], nums[1]))
# print(add(*nums))

nums = {"x": 15, "y": 25}

nums['z'] = 10
# del nums['z']
# print(nums.get('z', 0))
# --------------------------------------------------
# print(add(*nums))
# print(add(nums[0], nums[1]))
# --------------------------------------------------
# print(add(nums["x"], nums["y"]))
# print(add(**nums))
# --------------------------------------------------
def multiply2(*args):
    total = 1
    for arg in args:
        total *= arg

    return total

def apply(*args, operator):
    if operator == '*':
        return multiply2(*args)
    elif operator == '+':
        return sum(args)
    else:
        return "No valid operator provided to apply()."

print(apply(1, 3, 6, 7, operator="+"))
# print(apply(1, 3, 5, "+"))  # Error
