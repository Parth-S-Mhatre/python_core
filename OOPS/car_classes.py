class Car:
    def __init__(self,model,speed):
        self.model=model
        self.speed=speed

    def drive(self):
        print(f"the car has {self.model} and its {self.speed} ")
    
    def stop(self):
        print(f"The {self.model} has stop")