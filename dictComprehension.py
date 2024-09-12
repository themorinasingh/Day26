import random
names = ["Tom", "Susan", "Mike", "John", "Eleanor", "Dave", "Caroline"]

students = {student:random.randint(1, 100) for student in names }
print(students)
passing_students = {student:score for (student, score) in students.items() if score > 60}
print(passing_students)