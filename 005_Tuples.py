# Create a Tuple Using ()
import this


a = (11,22,33,44,55,55)

b = () #Empty Tuple
c = (2,) # tuple with single element; a=(3) this is not tuple its become int,string
print(type(b))

# For counting 
print('Count ', a.count(55))

# For index
print('index : ',a.index(44))

# Tuple Slicing 
print(a[1::2])

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple[1])

# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
