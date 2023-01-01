def greater_than_2(n):
    if  n>2:
        return True
    else:
        return False

h1 = [1,2,3,4,5, 0,-1,-2]
L1 = list(filter(greater_than_2, h1))
print(L1)