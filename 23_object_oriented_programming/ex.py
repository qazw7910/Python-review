student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}

def average(sequence):
    return sum(sequence) / len(sequence)

print(average(student['grades']))

class Student:
    def __init__(self, name:str, *grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

student = Student("Bob", 36, 67, 90, 100, 100)
print(student.name)
print(student.average())
#------------------------------------------------------------

