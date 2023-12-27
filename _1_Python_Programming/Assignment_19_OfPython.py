# Assignment- 19 of this Python Course.

"""

***** Questions On – While loop iterative control *****

    Questions:

        1-> Write a python script to print first 10 even natural numbers.
        2-> Write a python script to print first 10 even natural numbers in reverse order.
        3-> Write a python script to print squares of first 10 natural numbers.
        4-> Write a python script to print cubes of first 10 natural numbers.
        5-> Write a python script to print first 10 multiples of 5.

    Answers:

        => All the answers are out of the Comment box.


"""

print("Assignment- 19 of this Python Course.\n")

# Answer-1:
print("Solution of question-1")
i = 0
while i < 10:
    i += 1
    print(i * 2)

# Answer-2:
print("\nSolution of question-2")
i = 10
while i >= 1:
    print(i * 2)
    i -= 1

# Answer-3:
print("\nSolution of question-3")
i = 0
while i < 10:
    i += 1
    print(i * i)

# Answer-4:
print("\nSolution of question-4")
i = 1
while i <= 10:
    print(i * i * i)
    i += 1

# Answer-5:
print("\nSolution of question-5")
i = 0
while i < 10:
    i += 1
    print(i * 5)
