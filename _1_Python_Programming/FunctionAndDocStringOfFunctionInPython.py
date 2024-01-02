"""
Notes:-
    => Functions and DocString of Function in python.
        -> Python Functions is a block of statements that return the specific task. The idea is to put some
        commonly or repeatedly done tasks together and make a function so that instead of writing the
        same code again and again for different inputs, we can do the function calls to reuse code
        contained in it over and over again.

    => Some Benefits of Using Functions
        -> Increase Code Readability
        -> Increase Code ReUsability

    => Types of Functions in Python
        -> There are mainly two types of functions in Python.
            *-> Built-in library function: These are Standard functions in Python that are available to use.
            *-> User-defined function: We can create our own functions based on our requirements.

    => Creating a Function in Python
        -> We can create a user-defined function in Python, using the def keyword. We can add any type of
        functionalities and properties to it as we require.

        like as:-
                # A simple Python function

                def fun():
                  print("Welcome to CodingWill")

    => Calling a  Python Function
        -> After creating a function in Python we can call it by using the name of the function followed by
        parenthesis containing parameters of that particular function.

        like as:-
            # A simple Python function
            def fun():
                print("Welcome to GFG")

            # Driver code to call a function
            fun()

    => Python Function with Parameters
        -> If you have experience in C/C++ or Java then you must be thinking about the return type of the
        function and data type of arguments. That is possible in Python as well
        (specifically for Python 3.5 and above).

        => Defining and calling a function with parameters

            like as:-
                    def function_name(parameter: data_type) -> return_type:
                        '''Docstring'''
                        # body of the function
                        return expression

    And a lot more things about function is outside of the command box.

"""


# Practice on Functions and DocString of Function in python.

# Practice on Function with nature Take nothing, Return nothing.
def function1():
    """This function is used to print sum of Two numbers only."""
    a = int(input("Enter first number here: "))
    b = int(input("Enter second number here: "))
    print("The sum of a and b is: ", a + b)


print("This is my function, with nature Take nothing, Return nothing.")
function1()
print(function1.__doc__)  # this line of code is used to print docString of function.


# Practice on Function with nature Take something, Return nothing.
def function2(a, b):
    print("The sum of a and b is: ", a + b)


print("\nThis is my function, with nature Take something, Return nothing.")
function2(12, 13)


# Practice on Function with nature Take nothing, Return something.
def function3():
    return 10 + 20


print("\nThis is my function, with nature Take nothing, Return something.")
k = function3()
print("The sum of 10 and 20 is: ", k)


# Practice on Function with nature Take something, Return something.
def function3(a, b):
    return a + b


print("\nThis is my function, with nature Take something, Return something.")
k = function3(10, 20)
print("The sum of 10 and 20 is: ", k)
