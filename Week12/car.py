from __future__ import annotations

class Car:
    def __init__(self,make:str,model:str,year:int,odometer:int):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = odometer

    def __repr__(self)->str:
        return f'Make: {self.make.title()}\nModel: {self.model.title()}\nYear: {self.year}'

    def update_odometer(self,mileage:int):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print('Nuh uh! Can\'t roll back odometer')

    def add_to_odometer(self,mileage:int):
        self.odometer += mileage

    def read_odometer(self):
        print(f'odometer reading is at {self.odometer}')

class Battery:
    def __init__(self,battery_max:int):
        self.battery_max = battery_max

    def changeBatterySize(self,battery_max:int):
        if battery_max >= self.battery_max:
            self.battery_max = battery_max
        else:
            print('Can\'t make battery worse')

    def describe(self):
        print(f'This battery is a {self.battery_max}-KWh battery')

    def getRange(self):
        print(f'This battery\'s range is {3.75*self.battery_max} Km')

class ElectricCar(Car):
    def __init__(self,make:str,model:str,year:int,odometer=0):
        super().__init__(make,model,year,odometer)
        self.battery = Battery(40)

    def gas_tank(self):
        print('YOU ARE DUMB THIS IS ELECTRIC')

# car1 = Car('big','fast',2100,0)
# car1.read_odometer()
# car1.update_odometer(100)
# car1.read_odometer()
# car1.update_odometer(100)

Ecar1 = ElectricCar('big','fast',2100,0)
print(Ecar1)
print()
Ecar1.read_odometer()
print()
Ecar1.update_odometer(100)
Ecar1.read_odometer()
print()
Ecar1.update_odometer(10)
Ecar1.read_odometer()
print()
Ecar1.add_to_odometer(150)
Ecar1.read_odometer()
print()
Ecar1.gas_tank()
print()
Ecar1.battery.describe()
print()
Ecar1.battery.getRange()
print()
Ecar1.battery.changeBatterySize(20)
print()
Ecar1.battery.changeBatterySize(150)
Ecar1.battery.getRange()