"""
Notes:-
    => Decision control statement in Python.

            *-> if
            *-> if-else
            *-> if-elif-else
            *-> if-else ladder
            *-> Nested if-else
            *-> Short Hand if-else Notation

    ==> Some points:-
        => Decision control:
             -> The if-else statement in python is used to perform the operations based on some specific condition.
             -> The operations specified in if block are executed if and only if the given condition is true.
             ->  if, elif and else are the keywords in python.

"""
# Practice on Decision control statement.

# Solve this quick quiz no-1.
print("Solution of quick quiz no-1")
"""
Write a python script to tell if the value of a and b both are the same as well as what is the value of a and b.
"""
a = int(input("Enter value of A : "))
b = int(input("Enter value of B : "))
if a == b:
    print("A is equal to B")
print("The value of a= %d and b= %d" % (a, b))

# Solve this quick quiz no-2.
print("Solution of quick quiz no-2\n")
"""
Write a python script to check age for the driving.
"""
age = int(input("Enter your age here : "))
if 8 <= age <= 80:
    if age >= 18:
        print("you can drive.")
    else:
        print("You can't drive.")
else:
    print("You are not eligible for driving skills.")

# Solve this quick quiz no-3.
print("Solution of quick quiz no-3\n")
"""
Write a python script to check a greater number between two numbers as well as print if the value are same.
"""
a = int(input("Enter value of A : "))
b = int(input("Enter value of B : "))
if a == b:
    print("A and B both are the same.")
elif a > b:
    print("A is Greater than B.")
else:
    print("B is Greater than A")

# Solve this quick quiz no-4.
print("Solution of quick quiz no-4\n")
"""
Write a python script to check a greater number between three as well as print if the value are same.
"""
a = int(input("Enter value of A : "))
b = int(input("Enter value of B : "))
c = int(input("Enter value of C : "))
if a == b == c:
    print("All the value are same.")
elif a > b:
    if a > c:
        print("A is Greater.")
    else:
        print("C is Greater.")
else:
    if b > c:
        print("B is Greater.")
    else:
        print("C is Greater.")

# Solve this quick quiz no-5.
print("Solution of quick quiz no-5\n")
"""
Write a python script to check a number is positive or non-positive.
"""
x = int(input("Enter your number : = "))
print("Number is positive") if x > 0 else print("Number is non-Positive")
