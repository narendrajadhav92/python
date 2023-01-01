a = { 1: 'naren', 2: 'sam', 3: 'adam'}
b = {55:'justice'}
c = {35 :99}
# copy() will copy the list
#a = b.copy()
#print('A : ',a)

# update 
a.update(b)
print(a)

# items() will return  list of key value pair tuple
print('a.items() :',a.items())

# keys() will return keys list
print(a.keys())

# values()
print(a.values())

#D.pop(k[,d]) -> v, remove specified key and return the corresponding value.

#If key is not found, default is returned if given, otherwise KeyError is raised
c = a.pop(2,25)
print('pop() ',c)

#popitem will remove the last element, it takes 0 argument
a.popitem()
print(a)

#clear()  will clear the list {}
#b.clear()


#merging two lists 
z = {**a , **b}
print('Merged list : ', z)
print(z[55])