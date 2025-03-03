# Create a Class with instance attributes

# class Vehicle:
#     def __init__(self , max_speed ,  mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage
    
# Car = Vehicle("538km/h" , 3 )
# print(Car.max_speed , Car.mileage)

# Create a Vehicle class without any variables and methods
# class Vehicle: 
#     pass

# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
# class Vehicle:

#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

# class Bus (Vehicle):
#     def details(self):
#         print(f"{self.name}")

# obj = Bus("Marco" , 140 , 25)
# obj.details()


# class Vehicle:

#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

# class Bus(Vehicle):
#     pass

# School_bus = Bus("School Volvo", 180, 12)
# print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

# Class Inheritance
# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"

# class Bus(Vehicle):
#     pass

# School_bus = Bus("Volvo" , 140 ,12)
# print(School_bus.seating_capacity(5))

# Define a property that must have the same value for every class instance (object)
# class Vehicle:
#     color = "White"
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
        

# class Bus(Vehicle):
#     pass

# class Car(Vehicle):
#     pass

# School_bus =  Bus("Volvo" , 130 , 18)
# print(School_bus.color)

#  Class Inheritance
# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity

#     def fare(self):
#         return self.capacity * 100

# class Bus(Vehicle):
#     def fare(self):
#         amount = super().fare()
#         amount += amount * 10 / 100
#         return amount

# School_bus = Bus("School Volvo", 12, 50)
# print("Total Bus fare is:", School_bus.fare())

# Check type of an object
# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity

# class Bus(Vehicle):
#     pass

# School_bus = Bus("School Volvo", 12, 50)
# print(type(School_bus))

# Determine if School_bus is also an instance of the Vehicle class
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
print(isinstance(School_bus, Vehicle))