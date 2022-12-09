add = lambda x, y: x + y


# print(add(5, 7))


def double(x):
    return x * 2


sequence = [1, 3, 5, 9]

doubled = [double(x) for x in sequence]
# print(doubled)

# doubled = map(double, sequence)
# print(list(doubled))

doubled = map(lambda x: x * 2, sequence)
print(list(doubled))
