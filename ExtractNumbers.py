#  [[(1,2,3,"abcdef")],["125",54165,"sdhgv"],8,9,6,7] extract the number 

data = [[(1,2,3,"abcdef")], ["125", 54165, "sdhgv"], 8, 9, 6, 7]

def extract_numbers(obj):
    numbers = []
    if isinstance(obj, (int, float)):  # direct number
        numbers.append(obj)
    elif isinstance(obj, (list, tuple)):  # nested sequence
        for item in obj:
            numbers.extend(extract_numbers(item))
    return numbers

result = extract_numbers(data)
print(result)
