"""
Notes:-
    => For-else loop in Python
        -> Python also allows us to use the else condition for loops. The else block just after for/while is
        executed only when the loop is NOT terminated by a break statement.

"""
# Practice on for-else loop iterative control statement.

print('Practice on for-else loop iterative control')
# Python program to demonstrate
# for-else loop

for i in range(1, 4): # start_Point   End_Point
    print(i)
else:  # Executed because no break in for
    print("No Break\n")