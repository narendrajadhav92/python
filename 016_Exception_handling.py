a = 5
b = 5

try :
    
    print(a /b) 
except NameError as exd :
    print('name not defined')
except TypeError as tyd :
    print('Type error is occured ')
except Exception as e :
    print('Problem Occured ; ', e)

#else will work when try block donot have error.

else :
    print("Try : has sucessfully worked")
finally :
    print('Server DataBase Closed')