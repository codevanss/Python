rows = int(input("Enter number of rows: "))

start = 1
for i in range(1, rows + 1):
    num = start
    for j in range(i):
        print(num, end=" ")
        num -= (i - j)
    print()
    start += 1
