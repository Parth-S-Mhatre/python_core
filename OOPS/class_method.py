class Student:
    count=0
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
        Student.count+=1
    def get_info(self):
        return f"Name: {self.name} Roll No:{self.roll_no}"
    @classmethod
    def get_count(cls):
        return f"total Number of students: {cls.count}"
student1=Student("Parth",41)
print(Student.get_count())
        