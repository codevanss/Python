def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

def binomial(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

# Input number of rows
rows = int(input("Enter number of rows: "))

for i in range(rows - 1, -1, -1):
    # Print leading spaces
    print("  " * (rows - i - 1), end="")
    
    # Print binomial coefficients
    for j in range(i + 1):
        print(f"{binomial(i, j):4}", end="")
    print()
