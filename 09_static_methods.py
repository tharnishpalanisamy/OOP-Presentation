class Student:
    def __init__(self, name):
        self.name = name

    # Does not receive self or cls
    @staticmethod
    def is_valid_age(age):
        return 16 <= age <= 60

# Call through the class
print(Student.is_valid_age(20))
print(Student.is_valid_age(10))

# Call through an instance
student = Student("Arun")
print(student.is_valid_age(25))
