# 3. Inheritance
# Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute 

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def full_name(self): 
        return f"{self.brand} {self.model}"

    


class ElectricCar(Car): 
    def __init__(self, brand, model,battery_life):
        self.battery_life = battery_life
        super().__init__(brand, model)


class NewElectricCar(Car): 
    def __init__(self,brand,model,battery_life,milage):
        self.milage = milage
        super().__init__(brand,model,battery_life)


print('using the ')
electric_car = ElectricCar("Tesla","model s","85kWh")
print('Brand :',electric_car.brand)
print('Model :',electric_car.model)
print('Battery Life :',electric_car.battery_life)
print('Full Name :',electric_car.full_name())


