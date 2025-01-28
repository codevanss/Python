#Question:- A company insures its drivers in the following cases 
# If the driver is married
# If the driver is unmarried , male and above 30 years of age
# If the driver is unmarried , female and above 25 years of age
# In all the cases , the driver is not insured. If the martial status,sex and age as a input, write a program to determie whether the driver should be insured or not

print("Enter Every Input in lowercase")
Martial_status = input("Enter Your Martial Status : ")
Gender = input("Enter Your Gender : ")
Age = int(input("Enter Your Age : "))

if ((Martial_status == "unmarried" or "u") and (Gender =="male" or "m") and (Age > 30)):
    print("You are insured")
elif ((Martial_status == "unmarried" or "u") and (Gender =="female" or "f") and (Age > 25)):
    print("You Are insured")
elif (Martial_status == "married" or "m"):
    print("You are Insured")
else:
    print("Your are not insured")
