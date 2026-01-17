# Solution of Problem no 1 & 2

# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.z
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    # Problem: Add a method to the Car class that displays the full name of the car (brand and model)
    def full_name(self) :
        return f"{self.brand} {self.model}"




my_car = Car("Toyota","Fortunor")
print('my car ',my_car.brand)
print('my car ',my_car.model)

my_new_car = Car("Tata","safari")
print(my_new_car.full_name())

