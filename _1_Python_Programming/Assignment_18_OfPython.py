# Assignment- 18 of this Python Course.

"""

***** Questions On – While loop iterative control *****

    Questions:

        1-> Write a python script to print “Computer” 5 times on the screen.
        2-> Write a python script to print first 10 natural numbers.
        3-> Write a python script to print first 10 natural numbers in reverse order.
        4-> Write a python script to print first 10 odd natural numbers.
        5-> Write a python script to print first 10 odd natural numbers in reverse order.

    Answers:

        => All the answers are out of the Comment box.


"""

print("Assignment- 18 of this Python Course.\n")

# Answer-1:
print("Solution of question-1")
i = 0
while i < 5:
    i += 1
    print(i, "-> Computer")

# Answer-2:
print("\nSolution of question-2")
i = 1
while i <= 10:
    print(i)
    i += 1

# Answer-3:
print("\nSolution of question-3")
# First way to done this question.
i = 1
while i <= 10:
    print(11 - i)
    i += 1

# First way to done this question.
# i = 10
# while i >= 1:
#     print(i)
#     i-=1

# Answer-4:
print("\nSolution of question-4")
i = 1
while i <= 10:
    print(i * 2 - 1)
    i += 1

# Answer-5:
print("\nSolution of question-5")
i = 10
while i >= 1:
    print(i * 2 - 1)
    i -= 1
