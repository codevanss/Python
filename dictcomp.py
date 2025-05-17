# #create a dictionary where key are number and their values are cube from 1 to 5
dictt={x:x*x*x for x in range(1,6)}
print(dictt)

#create a dictionary from 1 to 10 where key are number and values are even and odd
dict={i:("even" if i%2==0 else "odd") for i in range(1,11)}
print(dict)