# All the use of Print() function in Python.

print("Welcome to Python.\n")

x = 10
print(x)
print("The value of x is : ", x)
print("The value of x is : %d\n"%x)

a = 100
b = 200
print("The sum of ", a, " and ", b, " is : ", (a + b))
print("The sum of %d and %d is : " % (a, b), (a + b))
print("The sum of %d and %d is : " % (a, b), (a + b), "\n")


print(10 * "Hello World\n")  # This will print Hello World 10 times.

var5 = "45"
var6 = "45"
print(10 * str((int(var5) + int(var6))))
