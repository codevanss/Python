arr = [9, 15, 22, 5, 4, 25, 28]
x = 28
found = False

for i in range(len(arr)):
    if arr[i] == x:
        found = True
        print(f"Element {x} found at index {i}")
        break

if not found:
    print("Element not found.")
