# Assignment- 13 of this Python Course.

"""

***** Questions On – Operators *****

    Questions:

        1-> Write a python script to remove the last digit from a given number. (for example, if user enters 2534
            then your output should be 253).
        2-> Write a python script to get the last digit from a given number. (for example, if user entered 2089 then
            your output should be 9).
        3-> Write a python script to swap data of two variables.
        4-> Write a python script which takes a three digit number from the user and display only its first digit.
        5-> Write a python script which takes a three digit number from the user and displays only its middle digit.

    Answers:

        => All the answers are out of the Comment box.


"""

print("Assignment- 13 of this Python Course.\n")

# Answer-1:
print("Solution of question-1")
n = int(input("Enter a number here : "))
print("The Answer of question 1 is : ", n//10, "\n")

# Answer-2:
print("\nSolution of question-2")
n = int(input("Enter a number here : "))
print("The Answer of question 2 is : ", n%10, "\n")

# Answer-3:
print("\nSolution of question-3")
a = 10
b = 20
print("The value of a is : ", a)
print("The value of b is : ", b)
a, b = b, a
print("Now the value of a after swapping is : ", a)
print("Now the value of b after swapping is : ", b)

# Answer-4:
print("\nSolution of question-4")
n = int(input("Enter a number here : "))
print("The Answer of question 4 is : ", n//100, "\n")

# Answer-5:
print("\nSolution of question-5")
n = int(input("Enter a number here : "))
n = n//10
print("The Answer of question 4 is : ", n%10, "\n")