"""
Notes:-
    => For loop iterative control statement in Python.
        -> In Python, there is no C style for loop, i.e., for (i=0; I <n; i++). There is a “for” loop which is similar
            to each loop in other languages. Let us learn how to use a loop for sequential traversals.

        => For Loops in Python
            -> Python For loop is used for sequential traversal i.e. it is used for iterating over an iterable
                like String, Tuple, List, Set, or Dictionary.

            -> Note: In Python, for loops only implement the collection-based iteration.

        -> Syntax of For loop in python.

            -> for var in iterable:
                    # statements

"""
# Practice on For loop iterative control statement.

# First Script to practice on For loop iterative control statement.
"""
=> Python For Loop in Python String
    -> This code uses a for loop to iterate over a string and print each character on a new line. The loop assigns 
    each character to the variable i and continues until all characters in the string have been processed.
"""
print('First script to practice on For loop iterative control')
for x in "Welcome to Python":
    print(x, end='')

# Second Script to practice on For loop iterative control statement.
"""
=> Python For Loop in Python String
    -> This code uses a for loop to iterate over a string and print each character on a new line. The loop assigns 
    each character to the variable i and continues until all characters in the string have been processed.
"""
print('\n\nSecond script to practice on For loop iterative control')
for x in "Ritik":
    print(x)

# Third Script to practice on For loop iterative control statement.
"""
=> Python For Loop with List
    -> This code uses a for loop to iterate over a list of strings, printing each item in the list on a new line. 
    The loop assigns each item to the variable I and continues until all items in the list have been processed.
"""
print('\nThird script to practice on For loop iterative control')
# Iterating over a list
l = ["Python", "with", "Ritik"]

for i in l:
    print(i)

# Forth Script to practice on For loop iterative control statement.
"""
=> Python For Loop in Python Dictionary
    -> This code uses a for loop to iterate over a dictionary and print each key-value pair on a new line. 
    The loop assigns each key to the variable i and uses string formatting to print the key and its 
    corresponding value.
"""
print('\nForth script to practice on For loop iterative control')
# Iterating over dictionary
print("Dictionary Iteration")

d = dict()

d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("% s % d" % (i, d[i]))

# Fifth Script to practice on For loop iterative control statement.
"""
=> Python For Loop with a step size
    -> This code uses a for loop in conjunction with the range() function to generate a sequence of numbers 
    starting from 0, up to (but not including) 10, and with a step size of 2. For each number in the sequence, 
    the loop prints its value using the print() function. The output will show the numbers 0, 2, 4, 6, and 8.
"""
print('\nFifth script to practice on For loop iterative control')
for i in range(0, 10, 2):  # start_Point   End_Point   Skip_value
    print(i)

# Sixth Script to practice on For loop iterative control statement.
"""
=> Python For Loop inside a For Loop
    -> This code uses nested for loops to iterate over two ranges of numbers (1 to 3 inclusive) and prints the 
    value of i and j for each combination of the two loops. The inner loop is executed for each value of i in 
    the outer loop. The output of this code will print the numbers from 1 to 3 three times, as each value of i is 
    combined with each value of j.
"""
print('\nSixth script to practice on For loop iterative control')
for i in range(1, 4):  # start_Point   End_Point
    for j in range(1, 4):
        print(i, j)

# Seventh Script to practice on For loop iterative control statement.
"""
=> Python For Loop with Zip()
    -> This code uses the zip() function to iterate over two lists (fruits and colors) in parallel. The for loop 
    assigns the corresponding elements of both lists to the variables fruit and color in each iteration. 
    Inside the loop, the print() function is used to display the message “is” between the fruit and color values. 
    The output will display each fruit from the list of fruits along with its corresponding color from the 
    colours list.
"""
print('\nSeventh script to practice on For loop iterative control')
fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "green"]
for fruit, color in zip(fruits, colors):
    print(fruit, "is", color)

# Eighth Script to practice on For loop iterative control statement.
"""
=> Python For Loop with Tuple
    -> This code iterates over a tuple of tuples using a for loop with tuple unpacking. In each iteration, 
    the values from the inner tuple are assigned to variables a and b, respectively, and then printed to the 
    console using the print() function. The output will show each pair of values from the inner tuples.
"""
print('\nEighth script to practice on For loop iterative control')
t = ((1, 2), (3, 4), (5, 6))
for a, b in t:
    print(a, b)

# Ninth Script to practice on For loop iterative control statement.
"""
=> Python for loop with range function
    -> The Python range() function is used to generate a sequence of numbers. Depending on how many arguments 
        the user is passing to the function, the user can decide where that series of numbers will begin and 
        end as well as how big the difference will be between one number and the next.range() takes mainly three 
        arguments. 

    -> start: integer starting from which the sequence of integers is to be returned
    -> stop: integer before which the sequence of integers is to be returned. 
    -> The range of integers ends at a stop – 1.
    -> step: integer value which determines the increment between each integer in the sequence.
"""
print('\nNinth script to practice on For loop iterative control')
# Python Program to
# show range() basics

# printing a number
for i in range(10):
    print(i, end=" ")

# performing sum of first 10 numbers
sum = 0
for i in range(1, 10):
    sum += i
print("\nSum of first 10 numbers :", sum)
