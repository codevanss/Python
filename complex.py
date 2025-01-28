# class Complex:
#     def __init__(self , real = 0.0 , imaginary = 0.0):
#         self.real = real 
#         self.imag = imaginary
#     def add(self , other):
#         z = Complex()
#         z.real = self.real + other.real
#         z.imag = self.imag +other.imag
#         return z
#     def __sub__(self , other):
#         z = Complex()
#         z.real = self.real-other.real
#         z.imag = self.imag-other.imag
#         return z
#     def display(self):
#         print(self.real ,self.imag)
#     def __str__(self):
#         return "hii"
# num1 = Complex(2.0,3.0)
# num2 = Complex(1.0,1.0)
# obj = num1.add(num2)
# obj1 = num1 - num2
# obj1.display()
# obj.display()
# print(obj)

# from abc import ABC, abstractmethod

# class Printer(ABC):
#     @abstractmethod
#     def print(self):
#         print("This is Printer class print function")
# class Laser(Printer):
#     def print(self):
#         print("Laser class print function")
# class Inkjet(Printer):
#     def print(self):
#         print("Inkjet class print function")

# d1 = Laser()
# d1.print()
# d2= Inkjet()
# d2.print()

class Student:
    def __init__(self, name,enroll, marks):
        self.name = name
        self.enroll = enroll
        self.marks = marks
    def calculate_total(self):
        return sum(self.marks.values())
    def avg(self):
        return self.calculate_total() / len(self.marks)
    def grade(self):
        average = self.avg()
        if average>= 90:
            return "A"
        elif average>=75:
            return "B"
        elif average>=50:
            return "C"
        else:
            return "fail"
    def display(self):
        print(f" Your name is {self.name} and enroll is {self.enroll}")
        print(f"total marks: {self.calculate_total()} , Avg : {self.avg():.2f} , Grade : {self.grade()}")
    
mark = {"science": 95 , "maths": 98 , "accounts" : 97}
s1 = Student("Parth" , 4 , mark)
print(s1.name)
print(s1.marks)
s1.display()