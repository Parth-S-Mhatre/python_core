from car_classes import Car

class Bmw(Car):
    def colour(self, color):
        print(f"The color is {color}")

# Assuming Car's constructor initializes the brand and speed attributes
car1 = Bmw("Porsche", 345)
car1.drive()  # Assuming `Car` class has a `drive` method
car1.stop()   # Assuming `Car` class has a `stop` method
car1.colour("Grey")
