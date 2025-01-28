#write a person class and initialize name and age and show 
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def show(self):
#         print(f"Name is {self.name} and age is {self.age}")

# Person("Vansh" , 20).show()

#Create a class Rectangle with attributes length and width. Add a method area to calculate and return the area of the rectangle.

# class Rectangle:
#     def __init__(self , length , breadth):
#         self.length = length
#         self.breadth = breadth
#     def area(self):
#         print(f"Area of rectangle is {self.length*self.breadth}")

# Area = Rectangle(2,3)
# print(Area.area())

# Create a base class Animal with a method speak that prints "Animal speaks". Create a derived class Dog that overrides this method to print "Dog barks".
# class Animal:
#     def speak(self):
#         print("Animal Speaks")
# class Dog(Animal):
#     def speak(self):
#         print("Dogs Bark")
# Sound = Dog()
# print(Sound.speak())


#create a bank account with private attribute balance . Provide method deposit and withdraw to modify the balance
# class Bank:
#     def __init__(self , Deposit , Withdraw , Balance):
#         self.__Balance = Balance
#         self.Deposit = Deposit
#         self.Withdraw = Withdraw
#     def show(self):
#         print(f"Previous Details : Balance = {self.__Balance}")
        
#     def withdraw(self , amount):
#         if amount>0 and amount<self.__Balance:
#             self.__Balance -= amount
#             print(f"Withdraw amount is {amount} , Remaining Balance is {self.__Balance}")
#         else:
#             print("Invalid")
#     def deposit(self , amount):
#         if amount>0:
#             self.__Balance+=amount
#             print(f"Deposit amount is {amount} and Current Balance is{self.__Balance} ")
#         else:
#             pass
#     def get_balance(self):
#         return self.__Balance
# Obj = Bank(0,0,10000)
# Obj.show()
# Obj.withdraw(5000)
# Obj.deposit(2000)

