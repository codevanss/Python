list1 = [1,2,32]
freq = {}
for i in list1:
    freq[i] = freq.get(i , 0)+1
for key in freq:
    if freq[key] >1:
        print("True")
        break
    else:
        print("false")
        break