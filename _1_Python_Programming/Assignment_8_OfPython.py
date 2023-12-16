# Assignment- 8 of this Python Course.

"""

***** Questions On – input from keyboard *****

    Questions:

        1-> Write a python script to take your name as input from the user and then print it.
        2-> Write a python script to take input two numbers from the user, then calculate their sum and display the
            result.
        3-> Write a python script which take the radius from the user and display area of the circle.
        4-> Write a python script to calculate square of a number. Number is entered by the user.
        5-> Write a python script which takes a character from the user and display its Unicode.

    Answers:

        => All the answers are out of the Comment box.


"""

print("Assignment- 8 of this Python Course.\n")

# Answer-1:
print("Solution of question-1")
myName = input("Enter your name here : ")
print("You have entered this name : ", myName)

# Answer-2:
print("\nSolution of question-2")
a = int(input("Enter first number here : "))
b = int(input("Enter second number here : "))
print("The sum of %d and %s is : %d" % (a, b, (a + b)))

# Answer-3:
print("\nSolution of question-3")
radius = int(input("Enter radius of a circle here : "))
print("The Area of circle according to the radius= %d is : " % radius, 3.14 * (radius * radius))

# Answer-4:
print("\nSolution of question-4")
square = int(input("Enter a number here : "))
print("The square of %d is : " % square, square * square)

# Answer-5:
print("\nSolution of question-5")
a = input("Enter a character here : ")
if len(a) == 1:
    print("The unicode of character= %c is : " % a, ord(a))
else:
    print("It's not a character value.")
