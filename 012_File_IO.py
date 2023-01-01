# append and write

f = open('samples.txt','a')
f.write('''\nThanks , \n Best of luck''')
f.close()

# to print
c = open('samples.txt')
d = c.readline()
print(d,end ='')
print(c.readline(),end = '')

c.close()
