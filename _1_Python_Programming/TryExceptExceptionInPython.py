"""
Notes:-
    => Try Except Exception in Python.
        -> Error in Python can be of two types i.e. Syntax errors and Exceptions. Errors are the problems in a
            program due to which the program will stop the execution. On the other hand, exceptions are raised
            when some internal events occur which changes the normal flow of the program.


    ==> Some of the common Exception Errors are : :-
        => IOError: if the file can’t be opened.
        => KeyboardInterrupt: when an un-required key is pressed by the user.
        => ValueError: when the built-in function receives a wrong argument.
        => EOFError: if End-Of-File is hit without reading any data.
        => ImportError: if it is unable to find the module.

    => Try Except in Python
        -> Try and Except statement is used to handle these errors within our code in Python. The try block is
            used to check some code for errors i.e. the code inside the try block will execute when there is no
            error in the program. Whereas the code inside the except block will execute whenever the program
            encounters some error in the preceding try block.

        -> Syntax of Try Except Exception.

            like as: try:
                        # Some Code
                    except:
                        # Executed if error in the
                        # try block

    => Else Clause.
        -> In Python, you can also use the else clause on the try-except block which must be present after all the
            except clauses. The code enters the else block only if the try clause does not raise an exception.

        -> Syntax of Try Except Else Exception.

            like as: try:
                         # Some Code
                     except:
                         # Executed if error in the
                         # try block
                     else:
                         # execute if no exception

    => Finally Keyword in Python.
        -> Python provides a keyword finally, which is always executed after the try and except blocks. The final
            block always executes after the normal termination of the try block or after the try block terminates
            due to some exceptions.

        -> Syntax of Try Except Else Exception.

            like as: try:
                         # Some Code
                     except:
                         # Executed if error in the
                         # try block
                     else:
                         # execute if no exception
                     finally:
                         # Some code .....(always executed)

"""

# Practice on Try Except in Python.

""" Code 1: No exception, so the try clause will run."""


# Python code to illustrate
# working of try()
def divide(x, y):
    try:
        # Floor Division : Gives only Fractional Part as Answer
        result = x // y
        print("Yeah ! Your answer is :", result)
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")


# Look at parameters and note the working of Program
divide(3, 2)

""" Code 1: There is an exception so only except clause will run."""


# Python code to illustrate
# working of try()
def divide(x, y):
    try:
        # Floor Division : Gives only Fractional Part as Answer
        result = x // y
        print("Yeah ! Your answer is :", result)
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")


# Look at parameters and note the working of Program
# print("\n")
divide(3, 0)

""" Code 2:  The other way of writing except statement, is shown below and in this way, it only accepts exceptions 
    that you’re meant to catch or you can check which error is occurring."""


# code
def divide(x, y):
    try:
        # Floor Division : Gives only Fractional Part as Answer
        result = x // y
        print("Yeah ! Your answer is :", result)
    except Exception as e:
        # By this way we can know about the type of error occurring
        print("The error is: ", e)


divide(3, "GFG")
divide(3, 0)


# Practice on Try Except Else Exception.
# Program to depict else clause with try-except

# Function which returns a/b
def AbyB(a, b):
    try:
        c = ((a + b) // (a - b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)


# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)


# Practice on Try Except Else Exception with Finally keyword.
# Python program to demonstrate finally

# No exception:- Exception raised in try block
try:
    k = 5 // 0  # raises divide by zero exception.
    print(k)

# handles zero division exception
except ZeroDivisionError:
    print("Can't divide by zero")

finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed')
