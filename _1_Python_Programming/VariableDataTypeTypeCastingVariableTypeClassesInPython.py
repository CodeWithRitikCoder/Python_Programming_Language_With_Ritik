"""
Notes:-
    => Python Variables
        -> Variables are containers that store information that can be manipulated and referenced later by the
            programmer within the code.
        -> In python, the programmer does not need to declare the variable type explicitly, we just need to assign the
            value to the variable.

        => It is always advisable to keep variable names descriptive and to follow a set of conventions while creating
            variables:
            -> Variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
            -> Variable name must start with a letter or the underscore character.
            -> Variables are case-sensitive.
            -> Variable name cannot start with a number.

    => Data Types

    => TypeCasting.
        -> Type conversion is a way to convert on data type into another data type.

        => Pre-defined functions in python.
            -> int()
            -> float()
            -> complex()
            -> bool()
            -> str()

        like as:-
                    -> Type conversion of int function. int function can convert all these types of value.
                        * int("45.6")
                        * int(3.32)
                        * int(True)
                        * int(False)

                    -> Type conversion of float function. float function can convert all these types of value.
                        * float("34.23")
                        * float("231")
                        * float(345)
                        * float(True)
                        * float(False)

                    -> Type conversion of complex function. complex function can convert all these types of value.
                        * complex("4.2+4j")
                        * complex(45)
                        * complex(45.3)
                        * complex(True)
                        * complex(False)
                        * complex("4.5")
                        * complex("34")

                    -> Type conversion of bool function. bool function can convert all these types of value.
                        * bool("True")
                        * bool("False")
                        * bool("Ritik")
                        * bool("2345")
                        * bool("3.4")
                        * bool(40)
                        * bool(-12)
                        * bool(4.3)
                        * bool("") -> Empty string no space can't convert.
                        * bool(" ") -> Every non-Empty string is True with white space.

                    -> Type conversion of str function. str function can convert all these types of value.
                        * str(45)
                        * str(45.12)
                        * str(True)
                        * str(False)
                        * str(45+6j)
                        * str("Ritik")

    => Variable Type Classes.

"""
a = 20  # Here this is our Int variable.
print("The value of a is : ", a)
print("This is the Type of a variable now : ", type(a))

a = 36.7
print("Now the a is : ", a)
print("This is the Type of a variable now : ", type(a))

a = "Ritik"
print("Now the a is : ", a, end=" ")

a = 'Programmer'
print(a)
print("This is the Type of a variable now : ", type(a))

a = True
print("Now the a is : ", a)
print("This is the Type of a variable now : ", type(a))

var1 = "Hello "
var2 = "World"
print(var1 + var2)

var3 = 5
# print(var1+ var3) #this will throw an error because of different type of variables.

var4 = 15
print("The sum of var3 and var4 is : ", (var3 + var4))

var5 = "45"
var6 = "45"
print("The sum of var5 + var6 is : ", (var5 + var6))  # This will do concatenate both the strings value. not plus as
# the integer.
print("The sum of var5 + var6 is : ", (int(var5) + int(var6)))

print(10 * "Hello World\n")  # This will print Hello World 10 times.

print(10 * str((int(var5) + int(var6))))


var7= "55"
print(type(var7)) # This will give you the type of variable var7.

var7= 34
print(type(var7)) # This will give you the type of variable var7.

