# lst = ['Virat' , 'Rohit' , 'KL Rahul' , 'Hardik' , 'Jasprit']
# d=dict.fromkeys(lst,50)
# print(d)

#merge dictionary
# dictt = { 'd1' : {'Mango' : 1 , 'Apple' : 2},
#           'd2' :{'Orannge' : 3 , 'Gauva' : 4},
#           'd3' : {'kiwi' : 5 , 'banana' : 6}
#         }
# d4 = {}

# for i in dictt:
#     d4.update(dictt)
# print(d4)

#Write a program to check dictionary is empty or not

# d1 = {'a' : 1 , 'b' : 2}
# d2 = {'c' : 3 , 'd' : 4}
# d3 = {}
# tpl = (d1,d2,d3)
# for i in tpl:
#     if(i):
#         print('Not Empty')
#     else:
#         print("Empty")

# if bool(d3):
#     print("true")
# else:
#     print("false")

# d1 = {'a' : 1 , 'b' : 2}
# d2 = {'c' : 3 , 'd' : 4}

# d3 = {**d1 , **d2}
# print(d3)

# d= { 'A':{"Salary" : 30000 , "Age" : 23},
#      'B' :{"Salary" : 23000 , "Age" : 34},
#      'C': {"Salary" : 20000 , "Age" : 26}
#     }
# lst = []
# for i in d.values():
#   lst.append(i["Salary"])

# print(lst)
# print("max",max(lst))
# print("min",min(lst))


lst = [1,2,2,3,3,3,4,4,4,4]
freq = {}

for i in lst:
    freq[i] = freq.get(i , 0)+1

print(freq)

