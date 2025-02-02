class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def display(self):
        print(f"Rectangle Length: {self.length}")
        print(f"Rectangle Width: {self.width}")
        print(f"Perimeter: {self.perimeter()}")
        print(f"Area: {self.area()}")

# Create an object of the Rectangle class
rect1 = Rectangle(5, 3)

# Call the display method to show the details
rect1.display()