# Assignment- 16 of this Python Course.

"""

***** Questions On – Decision Control *****

    Questions:

        1-> Write a python script to check whether a given number is a three digit or not.
        2-> Write a python script to check whether a given number is positive, negative or zero.
        3-> Write a python script to check whether a given quadratic equation has two real & distinct roots,
            real & equal roots or imaginary roots.
        4-> Write a python script to check whether a given year is a leap year or not.
        5-> Write a python script to print greater among three numbers. Print number only once even if the
            numbers are same.

    Answers:

        => All the answers are out of the Comment box.


"""

print("Assignment- 16 of this Python Course.\n")

# Answer-1:
print("Solution of question-1")
n = input("Enter a number here : ")
if len(n) == 3:
    print("It's a three digits number.")
else:
    print("It's not a three digits number.")


# Answer-2:
print("\nSolution of question-2")
n = int(input("Enter a number here : "))
if n == 0:
    print("Your have entered : %d" % n)
elif n > 0:
    print("%d is Positive number." % n)
else:
    print("%d is Non-positive number." % n)

# Answer-3:
print("\nSolution of question-3")
# about to come.

# Answer-4:
print("\nSolution of question-4")
n = int(input("Enter a Year here : "))
if (n % 4) == 0 and (n % 100) != 0:
    print("It's a Leap Year.")
else:
    print("It's not a Leap Year.")

# Answer-5:
print("\nSolution of question-5")
a = input("Enter first number here : ")
b = input("Enter second number here : ")
c = input("Enter third number here : ")
if a == b and a == c:
    print("All the numbers are the same.")
elif a > b:
    if a > c:
        print("Greater number is : ", a)
    else:
        print("Greater number is : ", c)
else:
    if b > c:
        print("Greater number is : ", b)
    else:
        print("Greater number is : ", c)