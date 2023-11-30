# String Slicing and it's functions in Python.

# What is String in Python.
"""
=> What is String in Python?
    => String is a data type in Python.
    => String is a sequence of character enclosed in quotes.

=> We can primarily write a string in these three ways.
    1-> Single quotes string --> a= 'Ritik'
    1-> Double quotes string --> a= "Ritik"
    1-> Triple quotes string --> a= '''Ritik'''

=> String Slicing in Python.
    => A String in python can be sliced for getting a part of the string.
    -> considered the following string:
        -> name= "|R|i|t|i|k|" ==> Length= 5 of this string.
                  (0 1 2 3 4) ==> indexing of the string.
                (-5 -4 -3 -2 -1) ==> second indexing of the string.

    -> The index in a string starts from (0) to (length-1) in python.
    -> In order to slicing a string, we can use the following syntax:
        -> sl= name[starting index : ending indexing]
        -> Starting indexing will include and ending indexing won't include.
        like:- name[0:3] -> this will return "Rit" -> character from 0 to 3
        like:- name[1:3] -> this will return "it" -> character from 1 to 3
        like:- name[50] -> this will throw an Error.
        like:- name[0:50] -> this will return "Ritik" -> character from 0 to 50

    -> Negative indices:- Negative indices can also be used as shown in figure above. -1 corresponds to the (length-1)
                          index -2 to (length-2).

    -> Slicing with skip value.
        -> we can provide a skip value as a part of our slice like this:-
                -> Word= "Amazing"
                -> word[1:6:1] --> This will return 'mazing' -> this will work by skipping 0 letter.
                -> word[1:6:2] --> This will return 'mzn' -> this will work by skipping 1 letter.
                -> word[:6] --> This will return 'amazing' -> this will take by default 0 at the starting index.
                -> word[0:] --> This will return 'amazing' -> this will take by default length at the ending index.
                -> word[::] --> This will return 'amazing' -> this will take by default 0:length:1
                -> word[-4:] -->
                -> word[-4:-2] -->
                -> word[::-1] --> This will return backward string.
                -> word[::-2] --> This will return backward string and skipping 1 character.

"""

# Practice on the string and string slicing.
myString = "Ritik is a good boy"

print("Practice on String")
print(myString)
print(myString[0:3])
print(myString[1:3])
# print(myString[50]) # => This will throw an error.
print(myString[0:50], "\n")

# Practice on the String slicing
print("Practice on String slicing")
print(myString[1:6:1])
print(myString[1:6:2])
print(myString[:6])
print(myString[0:])
print(myString[1:])
print(myString[:])
print(myString[-4:])
print(myString[-4:-2])
print(myString[-4:-1])
print(myString[::-1])
print(myString[::-2], "\n")

"""

    => String functions in python.
        -> Some of the most used functions to perform operations on or manipulate strings are:

        1-> len() function -> This function returns the length of the string.
            like:- len("Ritik") --> return 5

        2-> string.startswith("Ri") --> This function tells whether the variable string starts with the string "Ri" or not
            if string is "Ritik", it returns (true) for "Ri" sice Ritik ends with tik.
            
        3-> string.endswith("tik") --> This function tells whether the variable string ends with the string "tik" or not
            if string is "Ritik", it returns (true) for "tik" sice Ritik ends with tik.

        4-> string.count("c") --> Counts the total number of occurrence of an y character.
        
        5-> string.capitalize() --> This function capitalized the first character of a given string.
        
        6-> string.find(word) --> This function finds a word and returns the index of first occurrence of 
            that word in the string.
            
        7-> string.upper() --> This function will convert your entire string in to UPPER Case.
        
        8-> string.lower() --> This function will convert your entire string in to lower Case.
        
        9-> string.replace(oldWord, newWord) --> This function replaces the oldWord with newWord in the entire string.
"""

# Practice on String functions.
print("Practice on String functions")

print(type(myString))

print(myString.isalpha())  # => It means if there is a white space in your string then this will return False
                            # and if there is no space in your string then this will return True.
print(myString.isalnum()) # => It means if your string contains numeric value then this will return True
                            # other wise Flase.

print("This is the length of the string : ", len(myString))
print("Is my String starts With with 'Ritik' or not : ", myString.startswith("Ritik"))
print("Is my String starts with 'boy' or not : ", myString.startswith("boy"))
print("Is my String ends with 'boy' or not : ", myString.endswith("boy"))
print("Is my String ends with 'Ritik' or not : ", myString.endswith("Ritik"))

print("The count of 'i' is in my String : ", myString.count("i"))

myString = "ritik is a good boy"
print("This is your capitalize string : ", myString.capitalize())

print("At what index 'good ' is present in my string : ", myString.find("good"))

print("UPPER case of my String is : ", myString.upper())
myString = "RITIK is a good boy"
print("lower case of my String is : ", myString.lower())

myString = "Ritik is a good boy"
print("Replace function : ", myString.replace("good", "smart"))

myString = myString.replace("good", "smart")
print(myString)
