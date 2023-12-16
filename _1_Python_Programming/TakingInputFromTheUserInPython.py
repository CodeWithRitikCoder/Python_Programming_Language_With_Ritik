# Here python will take input as a string by-default.

"""
Notes:-
    => Taking input from user.
        -> input("Print message") -> this input function is used to take input from the user.
            * input() can take at most one argument of str type
            * input() always return Str type value.


    => Input variety of data.
        -> How to input a string?
            * s=input()
        -> How to input an int value?
            * x=int(input())
        -> How to input a float value?
            *  x=float(input())
        -> How to input a complex value?
            * x=complex(input())

    => Argument in input function.
        -> To provide direction for input you can pass a string argument in input method.
            * name = input("Enter your age : = ")
            * age = int(input("Enter your age : = "))

    => Taking multiple values.
        -> You can use multiple input() function to input multiple values.
        -> You can input multiple values using single input() function but it is little bit tricky and requires
            knowledge of Str class , which we will see in later lessons

"""

num1= input("Enter first number here : ") # Here this will store String value in var1
num2= input("Enter second number here: ") # Here this will store String value in var1

print("The sum of num1 and num2 is : ", int(num1)+ int(num2))

var1= int(input("\nEnter your Number here : "))  # Here this will store integer value in var1
print("The value of var1 is : ", var1)

var2= input("\nEnter your string here : ")
print("Your Entered String is this : ", var2)