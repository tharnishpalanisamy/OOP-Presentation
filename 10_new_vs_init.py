class Student:
    def __new__(cls, name):
        print("__new__() is called")
        return super().__new__(cls)

    def __init__(self, name):
        print("__init__() is called")
        self.name = name

student = Student("Arun")
print(student.name)
