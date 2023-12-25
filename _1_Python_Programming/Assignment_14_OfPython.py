# Assignment- 14 of this Python Course.

"""

***** Questions On – Operators *****

    Questions:

        1-> Write a python script to print True if the string ‘my’ is a member in a string
            entered by user.
        2-> Write a python script to input two strings from the user and display whether the two variables referred
            to the same object or not. Print True or False.
        3-> What will be the output of the python expression 5>10<5 ?
        4-> What will be the output of the python expression “Red” and “White” ?
        5-> What will be the output of the python expression True or False ?

    Answers:

        => All the answers are out of the Comment box.


"""

print("Assignment- 14 of this Python Course.\n")

# Answer-1:
print("Solution of question-1")
str = "My name is Ritik and I am from Atrauli (Aligarh)"
print("String is : ", str)
print("This string \"My\" is present of not in the main String : ", ("My" in str))
print("This string \"my\" is present of not in the main String : ", ("my" in str))

# Answer-2:
print("\nSolution of question-2")
str1 = input("Enter first string here : ")
str2 = input("Enter second string here : ")
print("Is entered string is same or not : ", (str1 is str2))

# Answer-3:
print("\nSolution of question-3")
print("The output of this 5>10<5 expression is : ", 5 > 10 < 5)

# Answer-4:
print("\nSolution of question-4")
print("The output of this 5>10<5 expression is : ", 'Red' and 'White')
print("The output of this 5>10<5 expression is : ", "White" and "Red")

# Answer-5:
print("\nSolution of question-5")
print("The output of this 5>10<5 expression is : ", True or False)
