from abc import ABC,abstractmethod
import math as m
class shape:
    def area(self):
        pass
class rectangle(shape):
    def __init__(self,length,breath):
        self.length=length
        self.breath=breath
    def area(self):
        return self.length*self.breath
class Circle(shape):
     def __init__(self,radius):
        self.radius=radius
     def area(self):
         return m.pi*m.pow(self.radius,2)

class Pizza(Circle):
    def __init__(self,toping,radius):
        self.toping=toping
        self.radius=radius
    

shapes=[Circle(1),rectangle(2,4),Pizza("Olifins",15)]

for shape in shapes:
    print(f"{shape.area()}cm^2")
        
        