# Assignment- 4 of this Python Course.

"""

Questions:

    1-> Write a python script containing a variable with some integer value, print value of this variable.
    2-> Write a python script to print the value of a variable. Variable contains your name as data.
    3-> Write a python script to print values of three variables, each in a new line. All three variables
        are filled with some integer values.
    4-> Create 5 variables each of them containing different types of data (like 35, True, “Learning”, 5.46, 3+4j, etc),
        Write a python script to print values of all the variables along with their data types.
    5-> Create three variables and assign current date to them, first variable contains day number, second variable
        contains month number and third variable contains year number. Write a python script to display date in
        standard way(e.g. 29/11/2022)

Answers:

    => All the answers are out of the Comment box.


"""

print("Assignment- 4 of this Python Course.\n")

# Answer-1:
a = 10
b = 20
print("Solution of question-1")
print("The value of a is : ", a)
print("The value of b is : ", b)
print("The value of a is : %d and b is : %d" % (a, b))
print("This sum of %d and %d is : %d" % (a, b, (a + b)))
print("This sum of %d and %d is : " % (a, b), (a + b), "\n")

# Answer-2:
name = "Ritik"
print("Solution of question-2")
print(name)
print("My name is : ", name, "\n")

# Answer-3:
x = 100
y = 200
z = 300
print("Solution of question-3")
print("First(1) way to sole question-3")
print("The value of X is : %d\nThe value of Y is : %d\nThe value of Z is : %d\n" % (x, y, z))

print("Second(2) way to sole question-3")
print("The value of X is : ", x)
print("The value of y is : ", y)
print("The value of z is : ", z, "\n")

# Answer-4:
j = 23
k = 12.5
l = True
m = "StringVariable"
n = 3 + 4j
print("Solution of question-4")
print("The value of J is : ", j, " of type : ", type(j))
print("The value of K is : ", k, " of type : ", type(k))
print("The value of L is : ", l, " of type : ", type(l))
print("The value of M is : ", m, " of type : ", type(m))
print("The value of N is : ", n, " of type : ", type(n), "\n")

# Answer-5:
day = 30
month = 11
year = 2023
print("Solution of question-5")
print("Today's date is : ", day, "\\", month, "\\", year, sep="")
print("Today's date is %d\\%d\\%d" %(day, month, year))
