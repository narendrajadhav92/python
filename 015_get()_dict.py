# dict.get(key) will return value , if not then return None 

a = { 1: 'naren', 2: 'sam', 3: 'adam'}
b = {2:'justice'}
print(a.get(55))

# return  default value  for giving default value
d = a.get(2,'Meta')
print(a)
print(d)

# setdefault will add item to the dict if not present

bb = a.setdefault(34,'paras')

print(a)
print(bb)

