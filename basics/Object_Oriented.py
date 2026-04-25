
# Classes and objects
# class Car : 
#     def __init__(self, carBrand, carModel):
#         self.brand = carBrand
#         self.model = carModel

# # Create an object of the Car class
# car1 = Car("Ford", "Mustang")

# print(car1.brand)  # Output: Ford
# print(car1.model)  # Output: Mustang c



# Class methods and self
# class Car :
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def display_info(self):
#         return f"Car Brand: {self.brand}, Car Model: {self.model}"

# # Create an object of the Car class
# car1 = Car("Toyota", "Corolla")

# # Call the display_info method
# print(car1.display_info())  # Output: Car Brand: Toyota, Car Model: Corolla



# Inheritance
# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand

#     def display_brand(self):
#         return f"Vehicle Brand: {self.brand}"

# class Car(Vehicle):
#     def __init__(self, brand, model):
#         super().__init__(brand)  # super() is used to Call the constructor of the parent class
#         self.model = model

#     def display_info(self):
#         return f"Car Brand: {self.brand}, Car Model: {self.model}"

# # Create an object of the Car class
# car1 = Car("Honda", "Civic")

# # Call the display_info method
# print(car1.display_info())  # Output: Car Brand: Honda, Car Model: Civic



# Encapsulation
# class BankAccount:
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.__balance = balance  # Private attribute

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             return f"Deposited: {amount}. New Balance: {self.__balance}"
#         else:
#             return "Deposit amount must be positive."

#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.__balance:
#             self.__balance -= amount
#             return f"Withdrew: {amount}. New Balance: {self.__balance}"
#         else:
#             return "Invalid withdrawal amount or insufficient funds."

#     def get_balance(self):
#         return f"Current Balance: {self.__balance}"

# # Create an object of the BankAccount class
# account1 = BankAccount("Alice", 1000)

# print(account1.account_holder)  # Output: Alice
# # print(account1.balance)  # This will raise an AttributeError because __balance is private
# # Perform some transactions
# print(account1.deposit(500))  # Output: Deposited: 500. New Balance : 1500
# print(account1.withdraw(200))  # Output: Withdrew: 200. New Balance: 1300
# print(account1.get_balance())   # Output: Current Balance: 1300



# Polymorphism
# class Car:

#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def get_brand(self):
#         return f"Car Brand: {self.brand}"

#     def full_name(self):
#         return f"{self.brand} {self.model}"

#     def fuel_type(self):
#         return "Petrol or Diesel"

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_capacity = battery_size

#     def fuel_type(self):
#         return "Electric"

# # Create objects of Car and ElectricCar classes
# car1 = Car("Toyota", "Camry")
# electric_car1 = ElectricCar("Tesla", "Model 3", "75 kWh")
# print(car1.full_name())  # Output: Toyota Camry
# print(car1.fuel_type())  # Output: Petrol or Diesel
# print(electric_car1.full_name())  # Output: Tesla Model 3
# print(electric_car1.fuel_type())  # Output: Electric




# Class Variables
# class Car:
#     total_cars = 0

#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#         Car.total_cars += 1

#     def get_brand(self):
#         return f"Car Brand: {self.brand}"

#     def full_name(self):
#         return f"{self.brand} {self.model}"

#     def fuel_type(self):
#         return "Petrol or Diesel"

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_capacity = battery_size

#     def fuel_type(self):
#         return "Electric"

# # Create objects of Car and ElectricCar classes
# car1 = Car("Toyota", "Camry")
# electric_car1 = ElectricCar("Tesla", "Model 3", "75 kWh")
# print(f"Total cars created: {Car.total_cars}")  # Output: Total cars created: 2




# Static Methods
# class Car:
#     total_cars = 0

#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#         Car.total_cars += 1

#     @staticmethod
#     def get_total_cars(self):    # do not use self in static method
#         return f"Total cars created: {Car.total_cars}"

#     @staticmethod
#     def fuel_type():
#         return "Petrol or Diesel"

# # Create objects of Car class
# car1 = Car("Toyota", "Camry")
# car2 = Car("Honda", "Civic")

# # print(car1.get_total_cars())   
# print(Car.get_total_cars(car1))
# print(car1.fuel_type())  



# Property Decorators
# class Car:
#     def __init__(self, brand, model):
#         self._brand = brand  # Use a single underscore to indicate a protected attribute
#         self._model = model

#     @property
#     def brand(self):
#         return self._brand

#     @brand.setter
#     def brand(self, value):
#         if isinstance(value, str) and value:
#             self._brand = value
#         else:
#             raise ValueError("Brand must be a non-empty string.")

#     @property
#     def model(self):
#         return self._model

#     @model.setter
#     def model(self, value):
#         if isinstance(value, str) and value:
#             self._model = value
#         else:
#             raise ValueError("Model must be a non-empty string.")

# # Create an object of the Car class
# car1 = Car("Toyota", "Camry")
# print(car1.brand)  # Output: Toyota
# print(car1.model)  # Output: Camry

# # Update the brand and model using the setter methods
# car1.brand = "Honda"
# car1.model = "Civic"
# print(car1.brand)  # Output: Honda
# print(car1.model)  # Output: Civic



# Class Inheritance and isinstance() function
# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand
#     def display_brand(self):
#         return f"Vehicle Brand: {self.brand}"
# class Car(Vehicle):
#     def __init__(self, brand, model):
#         super().__init__(brand)
#         self.model = model
#     def display_info(self):
#         return f"Car Brand: {self.brand}, Car Model: {self.model}"
# # Create an object of the Car class
# car1 = Car("Honda", "Civic")
# # Check if car1 is an instance of Car and Vehicle classes
# print(isinstance(car1, Car))      # Output: True
# print(isinstance(car1, Vehicle))  # Output: True



# Multiple Inheritance
class A:
    def method_a(self):
        return "Method A from class A"

class B:
    def method_b(self):
        return "Method B from class B"

class C(A, B):
    def method_c(self):
        return "Method C from class C"

# Create an object of class C
c1 = C()    
print(c1.method_a())  # Output: Method A from class A
print(c1.method_b())  # Output: Method B from class B
print(c1.method_c())  # Output: Method C from class C
