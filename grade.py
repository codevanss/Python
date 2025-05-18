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