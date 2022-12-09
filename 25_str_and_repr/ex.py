class Person:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age


# Bob = Person("Bob", 35)
# print(Bob)

# ----------------------------------------------------------------

class Person:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person {self.name}, {self.age} years old"


bob = Person("Bob", 35)
print(bob)


# ----------------------------------------------------------------
class Person:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def __repr__(self):
        return (
            f'<Person({self.name}, {self.age})>'
        )

bob = Person("Bob", '35')
print(bob)
