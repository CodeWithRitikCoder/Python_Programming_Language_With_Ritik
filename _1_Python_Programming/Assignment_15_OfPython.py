# Assignment- 15 of this Python Course.

"""

***** Questions On – Decision Control *****

    Questions:

        1-> Write a python script to check whether a given number is positive or non-positive.
        2-> Write a python script to check whether a given number is divisible by 5 or not.
        3-> Write a python script to check whether a given number is even or odd.
        4-> Write a python a script to print greater number between two numbers. Print number only once even if the
            number are same.
        5-> Write a python script to print two given words in dictionary order.

    Answers:

        => All the answers are out of the Comment box.


"""

print("Assignment- 15 of this Python Course.\n")

# Answer-1:
print("Solution of question-1")
n = int(input("Enter a number here : "))
if n > 0:
    print("%d is Positive number." % n)
else:
    print("%d is Non-positive number." % n)

# Answer-2:
print("\nSolution of question-2")
n = int(input("Enter a number here : "))
if (n % 5) == 0:
    print("%d is divisible by 5." %n)
else:
    print("%d is not divisible by 5." %n)

# Answer-3:
print("\nSolution of question-3")
n = int(input("Enter a number here : "))
if (n % 2) == 0:
    print("%d is Even number." %n)
else:
    print("%d is Odd number." %n)

# Answer-4:
print("\nSolution of question-4")
a = int(input("Enter first number here : "))
b = int(input("Enter second number here : "))
if a == b:
    print("%d and %d are the same number so we can't compare." %(a, b))
elif a > b:
    print("%d : is greater number." %a)
else:
    print("%d : is greater number." % b)


# Answer-5:
print("\nSolution of question-5")
a = input("Enter first word here : ")
b = input("Enter first word here : ")
if a == b:
    print("%s and %s are the same String." %(a, b))
elif a > b:
    print(b, a)
else:
    print(a, b)
