rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    # Print spaces
    print(" " * (rows - i), end="")
    # Print stars
    print("*" * (2 * i - 1))
