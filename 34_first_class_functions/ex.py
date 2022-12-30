def calculate(*values, operator):
    return operator(*values)


def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return 'You fool!'


# result = calculate(20, 4, operator=divide)
# print(result)

def average(*values):
    return sum(values) / len(values)


# result = calculate(10, 20, 30, 40, operator=average)
# print(result)

# -- searching with first-class functions --

def get_friend_name(friend):
    return friend["name"]

def search(sequence, expected, finder):
    for element in sequence:
        if finder(element) == expected:
            return element
    raise RuntimeError(f'Could not find an element with {expected}')


friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27}
]


print(search(friends, 'Bob_Smith', get_friend_name))
