class Student:
    academic_yr = 2025

    def __init__(self, name, age, stream):
        self.name = name
        self.age = age
        self.stream = stream


student1 = Student("Parth", 18, "comps")
print(student1.name)
print(Student.academic_yr)
