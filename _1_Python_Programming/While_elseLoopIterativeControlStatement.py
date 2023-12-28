"""
Notes:-
    => While-else loop iterative control statement in Python.
        -> As discussed above, while loop executes the block until a condition is satisfied. When the condition
            becomes false, the statement immediately after the loop is executed. The else clause is only executed
            when your while condition becomes false. If you break out of the loop, or if an exception is raised,
            it won’t be executed.

    => Note: The else block just after for/while is executed only when the loop is NOT terminated by a break
        statement.

        -> Syntax of while loop in python.
            * while expression:
                    code to be Execute.
                else:
                    code to be Execute.


"""
# Practice on While-else loop iterative control statement.

# case first of while-else loop block
i = 0
while i < 4:
    i += 1
    print(i)
else:  # Executed because no break in for
    print("No Break\n")


# case first of while-else loop block
i = 0
while i < 4:
    i += 1
    print(i)
    break
else:  # Not executed as there is a break
    print("No Break")