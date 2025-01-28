# Design a class Employee with attributes name, age, and salary. Add a class variable company that stores the company's name. Write methods to display employee details and change the company name.
# class Employee:
#     Company_Name = "Aaloo.com"
#     def __init__(self,name ,age , salary):
#         self.name = name
#         self.age = age
#         self.salary = salary

#     @classmethod
#     def display(cls,name , age , salary):
#         Company_name = "CodeVanss"
#         print(Company_name)
#         return name,age, salary
       


# print(Employee.display("vansh" , 21 ,10000))

# class Employee:
#     Company_Name = "Aaloo.com"
#     def __init__(self,name ,age , salary):
#         self.name = name
#         self.age = age
#         self.salary = salary

#     def display_details(self):
#         print(f"{self.name} _ {self.age}_ {self.salary} , {Employee.Company_Name}")

#     @classmethod
#     def change_name(cls , new_name):
#         cls.Company_Name = new_name
#         print(new_name) 

# emp1 = Employee("Alice" ,30, 10000)
# emp2 = Employee("vnash" , 21, 102345)

# emp1.display_details()
# emp2.display_details()

# Employee.change_name("Ascii")
# emp1.display_details()
# emp2.display_details()

# Write a class Library to store a collection of books. Include methods to add a book, lend a book, and display the available books.
# class Library:
#     def __init__(self,add):
#         self.add = add

#     def lend(self ,available,lend):
#        available += self.add
#        remaining = available-lend
#        print(remaining)
# lib = Library(0)
# lib.lend(10 ,5)

class Library:
    def __init__(self):
        self.books = []

    def add_book(self , book_name):
        self.books.append(book_name)
        print(f"{book_name} has been added to library")
    
    def lend_book(self,book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"{book_name} has been out")
        else:
            print(f"{book_name} is not available")
    
    def display_books(self):
        if self.books:
            print("Available books:")
            for book in self.books:
                print(f"{book}")
        else:
            print("No books are available in the library")
library = Library()
library.add_book("Harry Potter")
library.add_book("Marvel")
library.add_book("Python")
library.display_books()
library.lend_book("Harry Potter")
library.display_books()

