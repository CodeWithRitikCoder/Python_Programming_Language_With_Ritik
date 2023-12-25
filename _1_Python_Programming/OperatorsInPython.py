"""
Notes:-
    => Operators in Python.

    => What is Operator in Python?
        -> An operator is a symbol used to perform operations on data.

    => Types of operator in Python.
        1-> Arithmetic operators. :- (+, -, *, /, %, ** and //)
        2-> Relational/Comparison operators. :- (>, <, >=, <=, == and !=)
        3-> Logical operators. :- (and, or and not)
        4-> Bitwise operators. :- (&, |, ^, ~, >> and <<)
        5-> Assignment operators. :- (=, +=, -=, *=, /=, //=, %=, **=, &=, |=, ^=, >>= and <<=)
        6-> Identity operators. :- (is and is not)
        7-> Membership operators. :- (in and not in)

    => Some notes on Operators.

        -> Division(/) :- Always return float result.
        -> Floor(//) :- Always return floor value int type or float type depending on operands
        -> +, * :- can be used str type values also.

    => Addition(+) operator.

        -> (+) is addition operator when operands are number of type:- (int, float, complex and bool).
        -> (+) is Concatenation operator when operands are value of type:- string.
        -> (+) Operation is invalid when applied between a number and string.

    => Multiply(*) operator.
        -> (*) is used to multiply two numbers.
        -> (*) is repetition operator when applied between a string and int value.

    => Relational operators.
        -> <, >, <= and >= :- inequality operators.
        -> == and != :- equality operators. (Never gives error)

        -> Relational operator always give result in The form of (True or False).
        -> When truth value is converted to int, it become 1 for True and 0 for False.
        -> Relational operator can also be used to compare two strings.
        -> Only == and != operators can be used between two compare type values.
        -> == and != never yield error.

    => Logical operators.
        -> and, or and not :- are the Logical operators.

        -> Logical operator must be written in lowercase only.

        => Table of (and) Logical operator.
            |-------------------------------|
            |   Condition       |   result  |
            |-------------------|-----------|
            |1. True and True   |   True    |
            |2. True and False  |   False   |
            |3. False and False |   False   |
            |4. False and True  |   False   |
            |5. True and  X     |   False   |
            |5. False and  X    |   False   |
            |-------------------------------|

        => Table of (or) Logical operator.
            |-------------------------------|
            |   Condition       |   result  |
            |-------------------|-----------|
            |1. True and True   |   True    |
            |2. True and False  |   True    |
            |3. False and False |   False   |
            |4. False and True  |   True    |
            |5. True and  X     |   True    |
            |5. False and  X    |   False   |
            |-------------------------------|

        => Table of (not) Logical operator.
            |-------------------------------|
            |   Condition       |   result  |
            |-------------------|-----------|
            |1. True and True   |   False   |
            |2. True and False  |   True    |
            |3. False and False |   False   |
            |4. False and True  |   True    |
            |5. True and  X     |   False   |
            |5. False and  X    |   False   |
            |-------------------------------|

        => Important points about logical operators.
            -> Every non-zero value :- True
            -> Every zero value :- False
            -> Every non-empty string :- True
            -> Every empty string :- False

            -> When operands are non-bool then result will also be non-bool.

        => Assignment operator.
            -> How to assign values to multiple variable in a single line.
                -> x, y, z = 3,4,5; No Error (Correct)
                -> x, y, z = 2, 3; Error
                -> x=4, y=3, z=10; Error

        => Identity operators
            -> It checks whether the two references referring to the same object or no.
            -> It result in True or False.

        => Membership operators
            -> These operators are applicable only on container(iterable).
            -> They result True or False.
            -> Container is a type which can contain multiple values and also iterable.

            -> int, float, complex, bool are not iterable.
            -> str, range, list, tuple, set, dict, are iterable.

"""
"""
1-> Arithmetic operators. :- (+, -, *, /, %, ** and //)
    
    -> + :- Addition operator.
    -> - :- Subtraction operator.
    -> * :- Multiply operator.
    -> / :- Division operator.
    -> % :- Modulus operator.
    -> ** :- Exponential operator.
    -> // :- Floor operator.
"""
# Practice on Arithmetic operator.
print("Practice on Arithmetic operator.")
a = 33
b = 3
print("Addition of %d and %d is : " % (a, b), (a + b))
print("Subtraction of %d and %d is : " % (a, b), (a - b))
print("Multiply of %d and %d is : " % (a, b), (a * b))
print("Division of %d and %d is : " % (a, b), (a / b))
print("Modulus of %d and %d is : " % (a, b), (a % b))
print("Exponential of %d and %d is : " % (2, 3), (2 ** 3))
print("Floor of %d and %d is : " % (a, b), (a // b))

""" 
2-> Relational operators. :- (>, <, >=, <=, == and !=)

    -> > :- Greater operator.
    -> < :- Lesser operator.
    -> >= :- Greater or equal to operator.
    -> <= :- Lesser or equal to operator.
    -> == :- Is equal to operator.
    -> != :- Is not equal to operator.
"""
# Practice on Relational operator.
print("\nPractice on Relational operator.")
a = 33
b = 3
print("%d is Greater from %d : " % (a, b), (a > b))
print("%d is Lesser from %d : " % (a, b), (a < b))
print("%d is Greater or equal to from %d : " % (a, b), (a >= b))
print("%d is Greater or equal to from %d : " % (20, 20), (20 >= 20))
print("%d is Lesser or equal to from %d : " % (a, b), (a <= b))
print("%d is Lesser or equal to from %d : " % (22, 22), (22 <= 22))
print("%d is equal to %d : " % (a, b), (a == b))
print("%d is not equal to %d : " % (a, b), (a != b))

"""
3-> Logical operators. :- (and, or and not)
    
    -> and :- And operator
    -> or :- or operator
    -> not :- not operator
"""
# Practice on Logical operator.
print("\nPractice on Logical operator.")
print("(20 >= 20) and (23 != 26) is : ", (20 >= 20) and (23 != 26))
print("(20 <= 25) and (23 != 23) is : ", (20 <= 25) and (23 != 23))
print("(30 <= 25) and (23 != 23) is : ", (30 <= 25) and (23 != 23))
print("1 and 1 is : ", (1 and 1))
print("1 and 0 is : ", (1 and 0))
print("0 and 1 is : ", (0 and 1))
print("0 and 0 is : ", (0 and 0))
print("True and True is : ", (True and True))
print("True and False is : ", (True and False))
print("False and True is : ", (False and True))
print("False and False is : ", (False and False))

"""
4-> Bitwise operators. :- (&, |, ^, ~, >> and <<)
    
    -> & :- Bitwise and operator.
    -> | :- Bitwise or operator.
    -> ^ :- Bitwise x-or/exclusive or operator.
    -> ~ :- Tiled operator.
    -> >> :- Left shift operator.
    -> << :- Right shift operator.
"""
# Practice on Bitwise operator.
print("\nPractice on Bitwise operator.")
a = 12
b = 6
print("Bitwise & of %d and %d is : " % (a, b), (a & b))
print("Bitwise | of %d and %d is : " % (a, b), (a | b))
print("Bitwise ^ of %d and %d is : " % (a, b), (a ^ b))

"""
5-> Assignment operators. :- (=, +=, -=, *=, /=, //=, %=, **=, &=, |=, ^=, >>= and <<=)
    
    -> = :- Equal operator.
    -> += :- Addition and equal operator.
    -> -= :- Subtract and equal operator.
    -> *= :- Multiply and equal operator.
    -> /= :- Divide and equal operator.
    -> //= :- Floor and equal operator.
    -> %= :- Modulus and equal operator.
    -> **= :- Exponential and equal operator.
    -> &= :- Bitwise And and equal operator.
    -> |= :- Bitwise Or and equal operator.
    -> ^= :- Bitwise X-or and equal operator.
    -> >>= :- Left shift and equal operator.
    -> <<= :- Right shift and equal operator.
"""
# Practice on Assignment operator.
print("\nPractice on Assignment operator.")
a = 23
print("The value of a after = operator is : ", a)
a += 2
print("Now the value of a after += operator is : ", a)
a -= 3
print("Now the value of a after -= operator is : ", a)
a *= 3
print("Now the value of a after *= operator is : ", a)
a /= 3
print("Now the value of a after /= operator is : ", a)
a //= 3
print("Now the value of a after //= operator is : ", a)
a %= 3
print("Now the value of a after %= operator is : ", a)
a **= 3
print("Now the value of a after **= operator is : ", a)

a = 12
b = 15
a &= b
print("Now the value of a after &= operator is : ", a)
a |= b
print("Now the value of a after |= operator is : ", a)
a ^= b
print("Now the value of a after ^= operator is : ", a)
a >>= b
print("Now the value of a after >>= operator is : ", a)
a <<= b
print("Now the value of a after <<= operator is : ", a)

"""
6-> Identity operators. :- (is and is not)

    -> is :- is operator.    
    -> is not :- is not operator.    
"""
# Practice on Identity operator.
print("\nPractice on Identity operator.")
# Working on String value
a = "Ritik"
b = "Ritik"
print("a is b :- ", a is b)
print("a is not b :- ", a is not b)
a = "Ritik"
b = "Lovely"
print("a is b :- ", a is b)
print("a is not b :- ", a is not b)
# Working on numeric value
a = 23
b = 23
print("a is b :- ", a is b)
print("a is not b :- ", a is not b)
a = 25
b = 23
print("a is b :- ", a is b)
print("a is not b :- ", a is not b)

"""
7-> Membership operators. :- (in and not in)
    
    -> in :- in operator.
    -> not in :- not in operator.
"""
# Practice on Membership operator.
print("\nPractice on Membership operator.")
st = "My name is Ritik and I ma the big fan of Kawasaki ninja ZX10R"
print("Is ZX10R is Present in the string st : ", "ZX10R" in st)
print("Is Kawasaki is Present in the string st : ", 'Kawasaki' in st)
print("Is Bullet is Present in the string st : ", '''Bullet''' in st)
print("Is Rolls Royce is Present in the string st : ", """Rolls Royce""" in st)
print("Is Ritik and is Present in the string st : ", """Ritik and""" in st)
