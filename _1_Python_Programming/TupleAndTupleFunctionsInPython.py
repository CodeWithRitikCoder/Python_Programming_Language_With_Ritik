# Tuple and Tuple Functions in Python.

# What is List in Tuple.
"""
=> What is Tuple in Python?
    -> A Tuple is an immutable data type in Python.
    -> it is as treat as list in python. but Tuple is immutable.
    -> Tuple denoted by Parentheses and list is denoted by square parses.
        like-> tp = () ==> Empty Tuple
               tp = (1,) ==> Tuple with only one element needs a comma.
               tp = (1, 7, 9) ==> Tuple with more than one element.

    -> Once defined a tuple elements cant be altered or manipulated.

=> Tuple functions.
    -> Consider the following Tuple.
        like:- tp = (1, 7, 9, 3)

    1-> tp.count(1) --> This function will return number of times 1 occurs in Tuple tp.
    1-> tp.index(1) --> This function will return the index of first occurrence of 1 in Tuple tp.



"""
# Practice on List
print("Practice on Tuple")

tp1 = (1, 7, 9, 1, 3)
print("This is my Tuple : ", tp1)
print(type(tp1))

# tp2 = [1] = 9 # => If you will tru to change the value of tuple this will throw an error.

# => If we want to create a tuple with one element
# tp2 = (1) # => We cant create like this, this will throw an error.
tp2 = (1,)  # => We can create like this, this wont throw an error.
print(tp2)

tp3 = () # => Empty tuple
print(tp3, "\n")

# Practice on List
print("Practice on Tuple functions")

print("The count of 1 in Tuple is : ", tp1.count(1))

print("The 9 is Present in Tuple at index : ", tp1.index(9))