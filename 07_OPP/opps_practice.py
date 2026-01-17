class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"{self.brand} {self.model}"
    

class ElectricCar(Car):
    # fature of the electric car is brand , model and battery_life using the inheritance concept i.e: using the previous car class

    def __init__(self,brand,model,battery_life):
        self.battery_life = battery_life
        super().__init__(brand,model)
    

my_car = Car("Tata","safari")
print('car brand: ',my_car.brand)
print('car model: ',my_car.model)
print('full name: ',my_car.full_name(),"\n")

my_new_car = Car("suzuki","Brezza")
print('car brand: ',my_new_car.brand)
print('car model: ',my_new_car.model)
print('full name: ',my_new_car.full_name(),"\n")

my_electric_car = ElectricCar("Tesla","model s","85kwh")
print('car brand: ',my_electric_car.brand)
print('car model: ',my_electric_car.model)
print('car battery life: ',my_electric_car.battery_life)
print('full name: ',my_electric_car.full_name(),"\n")


