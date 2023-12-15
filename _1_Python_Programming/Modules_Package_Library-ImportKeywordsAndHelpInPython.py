# Modules-Package-Library, import, keywords and help() in Python.

# Modules in Python.
"""
Modules : - It is a python file. It can contain instance objects, function
objects and class object.
"""

# Package in Python.
"""
Package : - Package is a collection modules and sub packages.
"""

# Library in Python.
"""
Library : - Library is a collection of packages.
"""

# Import in Python.
"""
When ever we want to use special functionality of Python then we can import that functionality.

like as:-
    # import A  # => We can also import A.py file like this and this will import every thing of this file at a time.
    from A import a  # => This will import only variable a of this A.py file.
    from A import b as var  # => This will import only variable b of this A.py file but we can use it as name var.
    from A import *  # => This will import whole things from the Python Module file.
    
"""

# keywords in Python.
"""
The reserved words of Python is called keywords in Python.

=> There are lots of keywords in Python.
likes as :- 

help> keywords
Here is a list of the Python keywords.
_______________________________________________________________________________
|    False      |       class        |       from         |        or         |
|    None       |       continue     |       global       |        pass       |
|    True       |       def          |       if           |        raise      |
|    and        |       del          |       import       |        return     |
|    as         |       elif         |       in           |        try        |
|    assert     |       else         |       is           |        while      |
|    async      |       except       |       lambda       |        with       |
|    await      |       finally      |       nonlocal     |        yield      |
|    break      |       for          |       not          |                   |
*******************************************************************************

and how to print keywords list in python, using Terminal of IDEs.

1-> Print keywords list using Terminal.
    -> step-1. Open Machine your terminal. 
    -> step-2. type python and hit enter to just in pyton mode your terminal.
    -> step-3. type help() and hit enter.s
    -> step-4. type keywords and hit enter.
    -> Then this will so you all the list of Python keywords on the terminal screen.
    
2-> Print keywords list using IDEs.
    -> The solution of this question if present out of the comment line,

"""

from keyword import kwlist as ritik, kwlist

print("This is the list of Python keywords.")
print(kwlist)

# help() in python.
"""
help() command is used to get python help and remember one thing this will work on the terminal or IDLE software of 
Python.
"""
