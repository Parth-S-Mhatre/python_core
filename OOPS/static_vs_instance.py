class Employee:
    def __init__(self,name,position):
        self.name=name
        self.position=position
    def get_info(self):                             #instance method
        return f"Name:{self.name} Position:{self.position}"
    @staticmethod
    def isvalid(position):                               #static method no need to create object
        valid_position=["Manager","Engineer","Assisant","Cook"]
        return position in valid_position


employee1=Employee("Parth","Manager")
print(employee1.get_info())
print(Employee.isvalid("Manager"))