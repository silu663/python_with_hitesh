# 3. Inheritance
# Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute 

class Car:
    def __init__(self,brand,model):
        self.__brand = brand # "__" privatise the veriable (encapsulation)
        self.model = model
    
    
    def get_brand(self):
        return self.__brand + "!"
    
    def full_name(self): 
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Ptrol or disel"

    


class ElectricCar(Car): 
    def __init__(self, brand, model,battery_life):
        self.battery_life = battery_life
        super().__init__(brand, model)

    
    def fuel_type(self):
        return "Electric charge"


class NewElectricCar(Car): 
    def __init__(self,brand,model,battery_life,milage):
        self.milage = milage
        super().__init__(brand,model,battery_life)


# print('using the the Car class')
# print('Brand :',electric_car.brand)
# print('Model :',electric_car.model)
# print('Battery Life :',electric_car.battery_life)
# print('Full Name :',electric_car.full_name())
# print(electric_car.__brand)

electric_car = ElectricCar("Tesla","model s","85kWh")
print(electric_car.get_brand())
safari =  Car("Tata","safari")
print(electric_car.fuel_type())
print(safari.fuel_type())




