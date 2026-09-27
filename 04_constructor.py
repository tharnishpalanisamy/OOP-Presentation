class Student:
    def __init__(self, name, age):
        # Set the initial values for this object
        self.name = name
        self.age = age

student1 = Student("Arun", 20)
student2 = Student("Rahul", 21)

print(student1.name, student1.age)
print(student2.name, student2.age)
