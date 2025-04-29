#Count the occurence of each character
lst = [1,2,2,3,3,3,4,4,4,4]
freq = {}

for i in lst:
    freq[i] = freq.get(i , 0)+1

print(freq)