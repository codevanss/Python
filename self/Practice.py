#Reverse each word in a given list of words
word=["hello" , "world" , "pyhton" , "rocks"]
ls2=[word[::-1] for word in word ]
print(ls2)


#Count the occurence of each character
lst = [1,2,2,3,3,3,4,4,4,4]
freq = {}

for i in lst:
    freq[i] = freq.get(i , 0)+1

print(freq)

#write a function to count alpha and digit
a = "james bond 007"
def count_alpha_num(a):
    d={"alphabet": 0 , "digit" : 0}
    for i in a:
        if i.isalpha():
            d["alphabet"]+=1
        elif i.isdigit():
            d["digit"]+=1
        else:
            pass
    return d
            
b = count_alpha_num(a)
print(b)