import random
import string

chars = " "+string.punctuation+string.digits+string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"chars :{chars}")
# print(f"key :{key}")

#ENCRYPT
plain_text = input("Enter a text you want to encrypt: ")
cipher_text = ""  

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index] 

print(f"Original message : {plain_text}")
print(f"Encrypted message : {cipher_text}") 
print("")
print("")
print("")
print("")
print("")
print("")

#DECRYPT
cipher_text = input("Enter a text you want to encrypt: ")
plain_text = ""  

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index] 

print(f"Encrypted message : {cipher_text}") 
print(f"Original message : {plain_text}")

