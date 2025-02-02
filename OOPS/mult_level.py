class Car:
    def drive(self):
        print("Car is driving")
class Volkswagen(Car):
    def company(self):
        print("This all are owned By Volkswagen")

class Porshe(Volkswagen):
    pass

class Audi(Volkswagen):
    pass

porshe_911=Porshe()
porshe_911.drive()
porshe_911.company()
audi_etron=Audi()
audi_etron.drive()
audi_etron.company()

