List_1 = [22,44,11,33,33,55,77,66]

#Reverse List
List_1.reverse()
print('Reversed list ', List_1)

# Index() 
print('index(55) : ', List_1.index(55))

# Sorting in order
List_1.sort()
print('Sorted list ',List_1)


# Append , to add in list
List_1.append(88)
print("append List", List_1)

# Insert(index, string) element at Index , it takes two argument
List_1.insert(1,99)
print(List_1)
print('Len() : ',len(List_1))

# pop for deleting : list.pop(index) , .pop() default "Last"
List_1.pop(2)
List_1.pop()
print(List_1)

# remove from list
List_1.remove(77)
print('dicacrd ',List_1)


# For copy the list 
List_2 = List_1.copy()
print("List 2 : ", List_2)

# to clear the complete List
List_1.clear()
print("clear List 1 ",List_1)

# To count element
print('Count ',List_2.count(33))

# .extend(List) will extend list
List_1.extend(set(List_2))
print('Extended list : ' , List_1)
