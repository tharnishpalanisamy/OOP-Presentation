class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # self refers to the object calling the method
    def introduce(self):
        print(f"Hi, I am {self.name} and I am {self.age} years old.")

student1 = Student("Arun", 20)
student2 = Student("Rahul", 21)

student1.introduce()
student2.introduce()
