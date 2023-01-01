from functools import reduce
def sum_num(a ,b):
    return a+b
a = reduce(sum_num , [1,2,3,4])
print(a)
