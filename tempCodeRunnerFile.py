d1 = {'a' : 1 , 'b' : 2}
d2 = {'c' : 3 , 'd' : 4}
d3 = {}
tpl = (d1,d2,d3)
for i in tpl:
    if(i):
        print('Not Empty')
    else:
        print("Empty")

if bool(d3):
    print("true")
else:
    print("false")

d1 = {'a' : 1 , 'b' : 2}
d2 = {'c' : 3 , 'd' : 4}

d3 = {**d1 , **d2}
print(d3)