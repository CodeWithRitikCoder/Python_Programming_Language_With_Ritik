"""
Notes:-
    => TCS (Transfer control statement) for loop iterative control statement in Python.
        -> There are three ways to use TCS with while loop in python.
            * break
            * continue
            * pass

    => Python For Loop with Break Statement
        -> Python break statement brings control out of the loop.

    => Python for Loop with continue Statements
        -> Loop control statements change execution from their normal sequence. When execution leaves a scope, all
            automatic objects that were created in that scope are destroyed. Python supports the following
            control statements.
        -> Python for Loop with Continue Statement

    => Python For Loop with Pass Statement
        -> The pass statement to write empty loops. Pass is also used for empty control statements, functions,
        and classes.

"""
# Practice on TCS with for loop iterative control statement.

# Practice on break TCS for loop iterative control statement
print("\nPractice on break TCS for loop iterative control")
for letter in 'PythonWithRitik':
    # break the loop as soon it sees 'e' or 's'
    if letter == 't' or letter == 'i':
        break
print('Current Letter :', letter)

# Practice on continue TCS for loop iterative control statement
print("\nPractice on continue TCS for loop iterative control")
# Prints all letters except 'e' and 's'
for letter in 'PythonWithRitik':
    if letter == 't' or letter == 'i':
        continue
    print('Current Letter :', letter)

# Practice on pass TCS for loop iterative control statement
print("\nPractice on pass TCS for loop iterative control")
for letter in 'PythonWithRitik':
    pass
print('Last Letter :', letter)