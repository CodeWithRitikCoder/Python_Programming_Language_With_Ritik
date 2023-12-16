# Assignment- 9 of this Python Course.

"""

***** Questions On – Simple calculation on user data *****

    Questions:

        1-> Write a python script to calculate simple interest.
        2-> Write a python script to calculate area of a rectangle.
        3-> Write a python script to calculate average of three numbers entered by user.
        4-> Write a python script to calculate volume of a cuboid.
        5-> Write a python script to take two numbers from (say x and y), now calculate
            xy and display result.

    Answers:

        => All the answers are out of the Comment box.


"""

print("Assignment- 9 of this Python Course.\n")

# Answer-1:
print("Solution of question-1")
amount = int(input("Enter amount here : "))
months = int(input("Enter months here : "))
interest = int(input("Enter interest here : "))
print("The interest is : ", (amount * months * interest) / 100)

# Answer-2:
print("\nSolution of question-2")
length = float(input('Enter length of the rectangle here : '))
breadth = float(input('Enter breadth of the rectangle here : '))
print("The area of rectangle is : ", length * breadth)

# Answer-3:
print("\nSolution of question-3")
firstNumber = float(input("Enter first number here : "))
secondNumber = float(input("Enter second number here : "))
thirdNumber = float(input("Enter third number here : "))
average = (firstNumber + secondNumber + thirdNumber * 100) / 300
print("The average of %0.1f, %0.1f and %0.1f is : " % (firstNumber, secondNumber, thirdNumber), average)

# Answer-4:
print("\nSolution of question-4")
length = float(input("Enter length of Cuboid here : "))
width = float(input("Enter width of Cuboid here : "))
height = float(input("Enter height of Cuboid here : "))
print("The volume of cuboid is : ", length * width * height)

# Answer-5:
print("\nSolution of question-5")
x = int(input("Enter the value of x here : "))
y = int(input("Enter the value of y here : "))
print("The result of xy is : ", x*y)
