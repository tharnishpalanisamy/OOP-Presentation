class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display_details(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

    def has_passed(self):
        return self.marks >= 40

student1 = Student("Arun", 75)
student2 = Student("Rahul", 32)

student1.display_details()
print("Passed:", student1.has_passed())

student2.display_details()
print("Passed:", student2.has_passed())
