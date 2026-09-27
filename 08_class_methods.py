class Student:
    college = "PSG College"

    def __init__(self, name):
        self.name = name

    # cls refers to the class itself
    @classmethod
    def change_college(cls, new_name):
        cls.college = new_name

    def display(self):
        print(f"{self.name} studies at {self.college}")

student1 = Student("Arun")
student2 = Student("Rahul")

student1.display()
student2.display()

Student.change_college("ABC College")

student1.display()
student2.display()
