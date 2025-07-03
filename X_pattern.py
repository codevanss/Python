# Get number of rows from the user
rows = int(input("Enter number of rows (odd number recommended): "))

# Loop through rows
for i in range(rows):
    for j in range(rows):
        if j == i or j == rows - i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
