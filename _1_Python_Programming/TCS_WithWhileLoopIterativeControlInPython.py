"""
Notes:-
    => TCS (Transfer control statement) While loop iterative control statement in Python.
        -> There are three ways to use TCS with while loop in python.
            * break
            * continue
            * pass


"""
# Practice on TCS with While loop iterative control statement.

# Practice on break TCS while loop iterative control statement
# Solve this quick quiz no-1.
print("Solution of quick quiz no-1")
"""
Write a python scrip to create a game in which you have three chance to enter Even number if you want to Won the game.
other wise you loose this game.
"""
i = 1
while i <= 3:
    evenNumber = int(input("Enter a Even number here: "))
    if evenNumber % 2 == 0:
        break
    i += 1

if i == 4:
    print("you lost the Game.")
else:
    print("You WON the Game.")


# Practice on continue TCS while loop iterative control statement
# Solve this quick quiz no-2.
print("Solution of quick quiz no-2")
"""
Write a python script to print 10 Even number which is mandatory and also if used enter odd number then do not print
any value.
"""
i = 1
while i <= 10:
    evenNumber = int(input("Enter a Even number here: "))
    if evenNumber % 2 == 1:
        continue
    else:
        print(i, "-> Number is Even: ", evenNumber)
        i += 1


# Practice on pass TCS while loop iterative control statement
# Solve this quick quiz no-3.
print("Solution of quick quiz no-3")
i = 1
if i <= 3:
    pass
print("Hello!.")