try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You can't divide a number by zero")
except ValueError:
    print("Enter numbers only")
except Exception:
    print("Something went wrong!")
finally:
    print("Do some clean up here")