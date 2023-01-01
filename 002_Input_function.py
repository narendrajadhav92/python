#a = input("Enter Your Name : ")
#a = a.capitalize()
#print(a)
from email.quoprimime import quote


_string = "0123456789"
print(_string[0:10:])
print(_string[-4:])
print("Lenght is",len(_string))

#for checking endswith
print(_string.endswith("9"))

#for count the characters
print(_string.count("56"))

#for finding index of a character
print(_string.find('012'))

# For replacing words in strings
dd = _string.replace('01','EN')
print(dd)



