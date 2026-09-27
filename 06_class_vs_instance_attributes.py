class Student:
    college = "PSG College"

    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Arun", 20)
student2 = Student("Rahul", 21)

# Instance attributes are unique to each student
print(student1.name)
print(student2.name)

# Class attribute is shared by all instances
print(student1.college)
print(student2.college)
print(Student.college)

# Changing the class attribute affects all objects
Student.college = "ABC College"

print(student1.college)
print(student2.college)
