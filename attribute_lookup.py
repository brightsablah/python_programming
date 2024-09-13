class Vehicle:
    def __init__(self, make):
        self.make = make  # Instance attribute
    
    def drive(self):
        return "Driving"

class Car(Vehicle):
    wheels = 4  # Class attribute

    def honk(self):
        return "Honk!"

# Create an instance of Car
my_car = Car("Toyota")

# Attribute lookup process:
print(my_car.make)     # Step 1: Found in the instance's __dict__ (instance attribute)
print(my_car.wheels)   # Step 2: Found in the class's __dict__ (class attribute)
print(my_car.drive())  # Step 3: Found in the parent class (inherited method)
print(my_car.honk())   # Step 2: Found in the class's __dict__ (instance method)
