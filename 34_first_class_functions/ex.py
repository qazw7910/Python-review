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


