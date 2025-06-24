rows = int(input("Enter number of rows: "))

# Calculate starting number for the last row
start = 1
for i in range(1, rows + 1):
    start += 1
start -= 1  # Adjust back

# Print the reverse pattern
for i in range(rows, 0, -1):
    num = start
    for j in range(i):
        print(num, end=" ")
        num -= (i - j)
    print()
    start -= 1
