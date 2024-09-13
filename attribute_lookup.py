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


# Inspecting __dict__

print(my_car.__dict__)  # Shows the instance attributes
# Output: {'make': 'Toyota'}

print(Car.__dict__)     # Shows the class attributes and methods
# Output (truncated): {'__module__': '__main__', 'wheels': 4, 'honk': <function honk>, ...}

print(Vehicle.__dict__) # Shows the parent class attributes and methods
# Output (truncated): {'__module__': '__main__', 'drive': <function drive>, ...}



# METHOD RESOLUTION ORDER (MRO)
print(Car.mro()) #[<class '__main__.Car'>, <class '__main__.Vehicle'>, <class 'object'>]
