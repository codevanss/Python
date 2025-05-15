# 1️. Reverse a String Without Using [::-1]
# Problem: Write a function to reverse a string manually.

def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str
print(reverse_string("hello"))  # Output: "olleh"