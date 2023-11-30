# Assignment- 5 of this Python Course.

"""

***** Questions On – import and keywords *****

    Questions:

        1-> Write a python script to print all the keywords on the screen.
        2-> Use help section on python shell to see all the keywords.
        3-> Create two Python files A0.py and A1.py, Create a variable in A1.py and assign some value to it.
            Write a python script to import A1 module in A0 and print value of the variable created in A0.py.
        4-> Out of all the keywords, name those keywords which are used as data.
        5-> What is the use of del keyword?

    Answers:

        => All the answers are out of the Comment box.


"""

print("Assignment- 5 of this Python Course.\n")

# Answer-1:
print("Solution of question-1")

import keyword

# from keyword import kwlist  # => We can also done this task.

print("This is the list of Python Keywords.\n", keyword.kwlist, "\n")

# Answer-2:
print("Solution of question-2\n")
"""
=> Print keywords list using Terminal.
    -> step-1. Open Machine your terminal. 
    -> step-2. type python and hit enter to just in pyton mode your terminal.
    -> step-3. type help() and hit enter.s
    -> step-4. type keywords and hit enter.
    -> Then this will so you all the list of Python keywords on the terminal screen.
"""

# Answer-3:
print("Solution of question-3\n")
"""
=> A0.py and A1.py file is the solution of this question.
    -> Your can check it out in the A0.py and A1.py file.
    -> I have solved this question using A0.py and A1.py file.
"""

# Answer-4:
print("Solution of question-4")
"""
There are only three keywords which can be used as data.
    1-> True
    3-> False
    3-> None
"""
t = True
f = False
n = None
print("T contains : ", t)
print("F contains : ", f)
print("N contains : ", n, "\n")

# Answer-5:
print("Solution of question-5")
"""
=> The use of (del) keyword in Python.
    -> (del)- keyword is used to delete created variable in Python.
    -> and if we don't want to delete any variable of python this don't worry python will automatically delete variable.
    
    like as: out of the comment lines.
"""
x = 20
print("The value of X is : ", x)
del x
# print("The value of X is : ", x) # => Now we can access variable X because of del x. if we will use it
# this will throw an error.
