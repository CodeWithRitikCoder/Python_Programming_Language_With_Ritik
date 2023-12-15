# Unicode in Python.

"""
Notes:-
    => What is Unicode in Python?
        -> The Unicode is character encoding and its goal to replace the existing
            character sets with its standard UTF.
        -> UTF - Unicode Transformed format.
        -> UTF - is the most commonly used character encoding.
        -> It is also background compatible with ASCII.

    => There are two types of Unicode in python.
        -> Alphabets Unicode
        -> Symbols Unicode and so on.....

    => and there are two functions in Python to get Unicode to character and character to Unicode.
        1. ord(character_value) -> to get character to Unicode.
        2. chr(Unicode_value) -> to get Unicode to character.

"""
print("Unicode in Python")

x = 'A'
print("The Unicode of 'A' is : ", ord(x))
print("The Unicode of 'a' is : ", ord('a'), "\n")

y = 97
print("The Character at 67 unicode is : ", chr(y))
print("The Character at 190 unicode is : ", chr(190))
print("The Character at 220 unicode is : ", chr(220))
print("The Character at 430 unicode is : ", chr(430))