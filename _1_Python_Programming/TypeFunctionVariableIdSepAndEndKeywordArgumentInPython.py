# Type function, variable id, sep='' keyword arguments and end='' keyword argument in Python.

# What is Type function in python.
"""
=> What is type function in Python?
    -> type function is used to be know the class type of variable in python.

    -> like as:- var1= 12
              print(type(var1)) ---> this will be the class type of "int"

              var2= "Ritik"
              print(type(var1)) ---> this will be the class type of "str"



"""
# Practice on type function.
print("Practice on type function")
var1= 10
print("The type of var1 is : ", type(var1))

var1= "Ritik"
print("Now the type of var1 is : ", type(var1))

var2= 23.3
print("The type of var2 is : ", type(var2))


"""
=> Variable Id.
    -> id is used to be know the which id is the variable is containing.
    
    -> like as:- var1= 10
                 print(id(var1))
                 
                 var2= 10
                 print(id(var2))
                 
                 var3= "Ritik"
                 print(id(var3))
                            
                 
"""
# Practice on variable id.
print("\nPractice on variable id")

var3= 10
print("The id is referred by var3 is : ", id(var3))

var4= 10
# This will refer as same id as referred by var3 because of both the variables have same object of integer class.
print("The id is referred by var3 as same as var4 is : ", id(var4))

var3= "Ritik"
print("Now the id is referred by var3 is : ", id(var3))




"""
=> Sep='' and end='' keyword argument in Python.


"""
# Practice on Sep='' and end='' keyword arguments.
print("\nPractice on Sep='' and end='' keyword arguments")

a= 10
b= 20
c= 30
d= 40
print("\nHere I am using sep='' keyword argument")
# by-default this will give one white space between the variables value.
print(a, b, c)
print(a, b, c, sep=', ')
print(a, b, c, sep='\' ')
print(a, b, c, sep=' - ')
print(a, b, c, sep=' -> ')
print(a, b, c, sep=' <- ')

print("\nHere I am using end='' keyword argument")
# by-default this will give line break after a print function finish.
print(a, b, c)
print(a, b, c, end=', ')
print(a, b, c, end='\' ')
print(a, b, c, end=' - ')
print(a, b, c, end=' -> ')
print(a, b, c, end=' <- ')