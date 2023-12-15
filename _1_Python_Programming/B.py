# solution of Question- 12
# and this is the second file of Question-12

# import A  # => We can also import A.py file like this and this will import every thing of this file at a time.
from A import a  # => This will import only variable a of this A.py file.
from A import b as var  # => This will import only variable b of this A.py file but we can use it as name var.
from A import *  # => This will import whole things from the Python Module file.

print("The value of A is : ", a)
print("The value of B is : ", var)

a = 200  # => We can also change the value a another variable of another class but this will not change original value.
print("The value of A is : ", a)
