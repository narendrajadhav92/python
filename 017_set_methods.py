#                  Set Method	Description
a = {1,2,3,4,5}
# add()	Adds an element to the set, takes exactly one argument
a.add(6)
#print(a)

# copy()	Returns a copy of the set
z = a.copy()
#print('z :', z)

# difference()	Returns a set containing the difference between two or more sets
b = {4,5,6,7,8}
dd = {1}
cc = {25}
print(a.difference(b,dd))

# difference_update()	Removes the items in this set that are also included in another, specified set
a.difference_update(b)
print('difference Update: ', a)

# update()	Update the set with another set, or any other iterable
a.update(z)
print('Update :', a)

# intersection()	Returns a set, that is the intersection of two or more sets
print(a.intersection(b,dd))

# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
#a.intersection_update(b,dd)
print('intersection update : ' ,a)


# isdisjoint()	Returns whether two sets have a intersection or not
# comes true when they have different items
print('is disjoint : ',a.isdisjoint(cc))

# issubset()	Returns whether another set contains this set or not
print('is subset :', dd.issubset(a))

# issuperset()	Returns whether this set contains another set or not
print('is superset of a : ', a.issuperset(dd))

# pop()	Removes an element from the set; cannot pop() to empty set, returns Key error
# set.pop() takes no arguments
a.pop()
print(a)

# remove()	Removes the specified element, gives KeyError when item not found
a.remove(2)
a.discard(33) # discard dont give error when item not present
print('After discarding a : ',a)

# union()	Return a set containing the union of sets
print('Union : ', a.union(z,b))

# symmetric_difference()	Returns elements rather than Intersection 
print(a.symmetric_difference(b))

# symmetric_difference_update()	inserts the symmetric differences from this set and another
b.symmetric_difference_update(a)
print('symmetric_difference_update : ',b)

# clear()	Removes all the elements from the set
print('clear() : ',a.clear())
print(type(a))