def divide(divedend, divisor):
    if divisor == 0:
        return ZeroDivisionError('Divisor cannot be 0.')

    return divedend / divisor


# grades = []
# try:
#     average = divide(sum(grades), len(grades))
#     print(average)
# except ZeroDivisionError as e:
#     print(e)
#     print("There are no grades yet in your list.")


# -- Built-in errors --

# TypeError: something was the wrong type
# ValueError: something had the wrong value
# RuntimeError: most other things


# grades = [90, 100, 85]
#
# try:
#     average = divide(sum(grades), len(grades))
# except ZeroDivisionError:
#     print("There are no grades yet in your list.")
# else:
#     print(f'the average was {average}')

# -- Doing something no matter what --

students = [
    {'name': 'Bob', 'grades': [75, 90]},
    {"name": "Rolf", "grades": []},
    {"name": "Jen", "grades": [100, 90]},
]
try:
    for student in students:
        name = student['name']
        grades = student['grades']
        average = divide(sum(grades), len(grades))
        print(f'{name} averaged {average}.')

except ZeroDivisionError:
    print(f"ERROR: {name} has no grades!")
else:
    print("-- All student averages calculated --")
finally:
    print("-- End of student average calculation --")
