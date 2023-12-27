# Assignment- 17 of this Python Course.

"""

***** Questions On – Match case Control *****

    Questions:

        1-> Write a python script to perform some operations like as:- Addition, Subtract, Multiply and division
            between two number.
        2-> Write a python script to check whether a given number is positive, negative or zero.
        3-> Write a python script to make a menu-driven program in which user has to choose one of the option from
            four given options - 1)Odd-Even, 2) positive-non positive, 3) simple interest, 4) Exit. Match and execute
            appropriate code on user selection.
        4-> Write a python script to take one data from user and evaluate the type of data. If the data is of int
            type then print Monday, if the data is of float type then print Tuesday, if the data is of complex
            type then print Wednesday, if the data is of type bool then print Thursday.
        5-> Write a python script to take a string from the user. If the string is a part of “Learning Computer
            Education” then print “One” if the string is a part of “Education” then print “Two” and if the string is
            a part of “services” then print “Three”.

    Answers:

        => All the answers are out of the Comment box.


"""

print("Assignment- 17 of this Python Course.\n")

# Answer-1:
print("Solution of question-1")
print("1-> for Addition.")
print("2-> for Subtraction.")
print("3-> for Multiply.")
print("4-> for Division.")
n = int(input("Enter your choice here: "))

match n:
    case 1:
        a = int(input("Enter your first number here: "))
        b = int(input("Enter your second number here: "))
        print('Addition of %d and %d is: ' % (a, b), (a + b))
    case 2:
        a = int(input("Enter your first number here: "))
        b = int(input("Enter your second number here: "))
        print('Subtraction of %d and %d is: ' % (a, b), (a - b))
    case 3:
        a = int(input("Enter your first number here: "))
        b = int(input("Enter your second number here: "))
        print('Multiply of %d and %d is: ' % (a, b), (a * b))
    case 4:
        a = int(input("Enter your first number here: "))
        b = int(input("Enter your second number here: "))
        print('Division of %d and %d is: ' % (a, b), (a / b))
    case _:
        print('Invalid choice!')

# Answer-2:
print("\nSolution of question-2")
n = int(input("Enter a number here: "))
match n:
    case n if(n == 0):
        print("Number is 0")
    case n if(n > 0):
        print("Number is Positive.")
    case n if(n < 0):
        print("Number is Negative")
    case _:
        print("Invalid value!")

# Answer-3:
print("\nSolution of question-3")
print("1-> to check number is Even and Odd")
print("2-> to check number is Positive or Non-positive.")
print("3-> to calculate simple interest.")
print("4-> to EXIT.")
n = int(input("Enter your choice: "))

match n:
    case 1:
        a = int(input("Enter a number here: "))
        if a % 2 == 0:
            print("Number is Even.")
        else:
            print("Number is Odd.")
    case 2:
        a = int(input("Enter a number here: "))
        if a == 0:
            print("Number is Zero(0).")
        elif a > 0:
            print("Number is Positive.")
        else:
            print("Number is Non-positive.")
    case 3:
        rupees = float(input("Enter your amount: "))
        interest = float(input("Enter interest rate: "))
        time = float(input("Enter time in Months/Year: "))
        print("The simple interest is : ", (rupees * interest * time) / 100)
    case 4:
        exit()
    case _:
        print("Invalid choice!")

# Answer-4:
print("\nSolution of question-4")
n = eval(input("Enter your data here: "))
match n:
    case n if type(n) == int:
        print("Monday.")
    case n if type(n) == float:
        print("Tuesday.")
    case n if type(n) == complex:
        print("Wednesday.")
    case n if type(n) == bool:
        print("Thursday.")

# Answer-5:
print("\nSolution of question-5")
n = input("Enter your string value here: ")
match n:
    case n if n == "Learning Computer Education":
        print("One")
    case n if n == "Education":
        print("Two")
    case n if n == "services":
        print("Three")
    case _:
        print("Invalid Value.")