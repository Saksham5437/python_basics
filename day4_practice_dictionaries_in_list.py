#Practing with lists and dictionaries with loops

students = [
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Bob", "age": 22, "grade": "B"},
    {"name": "Charlie", "age": 19, "grade": "C"},
    {"name": "David", "age": 21, "grade": "D"}
]

for student in students:
    print(student["name"], student["age"], student["grade"], sep = ", ")




 