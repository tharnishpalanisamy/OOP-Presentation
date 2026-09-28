class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"

    def __repr__(self):
        return f"Student(name='{self.name}', age={self.age})"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


student1 = Student("Arun", 20)
student2 = Student("Arun", 20)
student3 = Student("Rahul", 21)

print(student1)
print(repr(student1))

print(student1 == student2)
print(student1 == student3)