"""
Notes:-
    => Match case control statement in Python.

    => What is a ‘match-case’ statement?
        -> For developers coming from languages like C/C++ or Java know that there was a conditional
           statement known as Switch Case. This Match-Case is the Switch Case of Python
           which was introduced in Python 3.10. Here we have to first pass a parameter then try to
           check with which case the parameter is getting satisfied. If we find a match we will do
           something and if there is no match at all we will do something else.
        -> and there is no need to apply break; statement inside the match case block like as C/C++.

    ==> Some points:-

        => Pseudocode for Python match-case Statement
            -> The match statement is initialized with the match keyword creating a block and taking a
                parameter ( here the name is also a parameter ) and then steps down to the various cases
                using the case keyword and the pattern, for the pattern to match the parameter. The ” _  ” is
                the wildcard character which is run when nothing is matched.

    => Questions on Match case in python.

        => Q: What is the match-case statement in Python?
           A: The match-case statement, also known as pattern matching, is a feature introduced in Python 3.10.
           It provides a concise and expressive way to perform pattern matching on data structures,
           such as tuples, lists, and classes. It allows you to match the value of an expression against a
           series of patterns and execute the corresponding block of code for the matched pattern.

        => Q: How does the match-case statement differ from if-elif-else statements?
           A: The match-case statement is a more powerful and expressive construct compared to if-elif-else statements.
           While if-elif-else statements rely on boolean expressions, match-case statements can match patterns based
           on the structure and value of the data. Match-case statements provide a more structured and readable
           way to handle multiple conditions and perform different actions based on those conditions.

        => Q: What are the benefits of using the match-case statement?
           A: The match-case statement offers several benefits, including:
                * Conciseness: Match-case statements allow you to express complex branching logic in a concise and
                    readable manner.
                * Readability: Pattern matching makes the code more readable and self-explanatory, as it closely
                    resembles the problem domain.
                * Safety: Match-case statements provide exhaustive pattern matching, ensuring that all possible
                    cases are handled.

"""
# Practice on Match case control statement.

# Solve this quick quiz no-1.
"""
Code a python script to calculate:- Addition, Subtraction, Multiplication and division between two numbers.
"""

# print("1-> for Addition.")
# print("2-> for Subtraction.")
# print("3-> for Multiply.")
# print("4-> for Division.")
# n = int(input("Enter your choice here: "))
#
# match n:
#     case 1:
#         a = int(input("Enter your first number here: "))
#         b = int(input("Enter your second number here: "))
#         print('Addition of %d and %d is: ' % (a, b), (a + b))
#     case 2:
#         a = int(input("Enter your first number here: "))
#         b = int(input("Enter your second number here: "))
#         print('Subtraction of %d and %d is: ' % (a, b), (a - b))
#     case 3:
#         a = int(input("Enter your first number here: "))
#         b = int(input("Enter your second number here: "))
#         print('Multiply of %d and %d is: ' % (a, b), (a * b))
#     case 4:
#         a = int(input("Enter your first number here: "))
#         b = int(input("Enter your second number here: "))
#         print('Division of %d and %d is: ' % (a, b), (a / b))
#     case _:
#         print('Invalid choice!')

# Solve this quick quiz no-2.
n = eval(input("Enter your choice here: "))  # This eval() function will not change String value so this will throw an
# error
match n:
    case n if (type(n) == int):
        print("Integer bock of match case.")
    case n if (type(n) == float):
        print("Floating bock of match case.")
    case n if (type(n) == bool):
        print("Boolean bock of match case.")
    # case n if(type(n) == str):  //--> This will not take string value so this will throw an error.
    #     print("String bock of match case.")
    case _:
        print('Invalid choice!')
