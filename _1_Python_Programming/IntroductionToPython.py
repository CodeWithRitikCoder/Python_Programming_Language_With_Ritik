"""
Notes:-
    =>What is Python ?
        -> Python is a dynamically typed, General Purpose Programming Language that supports an object-oriented programming approach as well as a functional programming approach.
        -> Python is also an interpreted and high-level programming language.
        -> It was created by Guido Van Rossum in 1989.

    => Introduction To Python.
        -> Python is a widely used general-purpose, high level programming language. 
        It was created by Guido van Rossum in 1991 and further developed by the Python Software Foundation. 
        It was designed with an emphasis on code readability, 
        and its syntax allows programmers to express their concepts in fewer lines of code.
        
        -> Python is a programming language that lets you work quickly and integrate systems more efficiently.
        -> There are two major Python versions: Python 2 and Python 3. Both are quite different.
        
    => Beginning with Python programming:
    
        => 1) Finding an Interpreter:
            -> Before we start Python programming, we need to have an interpreter to interpret and run our programs. 
            There are certain online interpreters like https://ide.geeksforgeeks.org/ that can be used to run Python 
            programs without installing an interpreter.
            
            => Python For Windows:
                -> Windows: There are many interpreters available freely to run Python scripts like IDLE 
                (Integrated Development Environment) that comes bundled with the Python software downloaded from http://python.org/.
                
            => Python For Linux:
                -> Linux: Python comes preinstalled with popular Linux distros such as Ubuntu and Fedora. 
                To check which version of Python you’re running, type “python” in the terminal emulator. 
                The interpreter should start and print the version number.

            => Python For MacOS:
                -> macOS: Generally, Python 2.7 comes bundled with macOS. 
                You’ll have to manually install Python 3 from http://python.org/.

            => Installing Packages:
                -> To install packages in Python, we use the pip command.
                -> e.g. pip install "Package Name"
                
        => 2) Writing our first program:
            -> Just type in the following code after you start the interpreter.
                ->  # Script Begins
                    print("Introduction to Python.")
                    # Scripts Ends

                -> Output:
                    Introduction to Python.

        => Let’s analyze the script line by line.

            -> Line 1: [# Script Begins] In Python, comments begin with a #. This statement is ignored by the interpreter and serves as
            documentation for our code.
            -> Line 2: [print(“GeeksQuiz”)] To print something on the console, print() function is used.
            This function also adds a newline after our message is printed(unlike in C). Note that in Python 2, “print” is not a
            function but a keyword and therefore can be used without parentheses. However, in Python 3, it is a function and must be
            invoked with parentheses.
            -> Line 3: [# Script Ends] This is just another comment like in Line 1.

            -> Python designed by Guido van Rossum at CWI has become a widely used general-purpose, high-level programming language.

        => Prerequisites:

            -> Knowledge of any programming language can be a plus.

            -> Reason for increasing popularity
                1. Emphasis on code readability, shorter codes, ease of writing
                2. Programmers can express logical concepts in fewer lines of code in comparison to languages such as C++ or Java.
                3. Python supports multiple programming paradigms, like object-oriented, imperative and functional programming or procedural.
                4. There exists inbuilt functions for almost all of the frequently used concepts.
                5. Philosophy is “Simplicity is the best”.

        => LANGUAGE FEATURES

            -> Interpreted
                * There are no separate compilation and execution steps like C and C++.
                * Directly run the program from the source code.
                * Internally, Python converts the source code into an intermediate form called bytecodes which is then translated
                into native language of specific computer to run it.
                * No need to worry about linking and loading with libraries, etc.

            -> Platform Independent
                * Python programs can be developed and executed on multiple operating system platforms.
                * Python can be used on Linux, Windows, Macintosh, Solaris and many more.

            -> Free and Open Source; Redistributable
            -> High-level Language
                * In Python, no need to take care about low-level details such as managing the memory used by the program.

            -> Simple
                * Closer to English language;Easy to Learn
                * More emphasis on the solution to the problem rather than the syntax

            -> Embeddable
                * Python can be used within C/C++ program to give scripting capabilities for the program’s users.

            -> Robust:
                * Exceptional handling features
                * Memory management techniques in built

            -> Rich Library Support
                * The Python Standard Library is very vast.
                * Known as the “batteries included” philosophy of Python ;It can help do various things involving regular
                expressions, documentation generation, unit testing, threading, databases, web browsers, CGI, email, XML, HTML, WAV files,
                cryptography, GUI and many more.
                * Besides the standard library, there are various other high-quality libraries such as the Python Imaging
                Library which is an amazingly simple image manipulation library.
        
"""

# Script Begins

print("Introduction to Python.")

# Scripts Ends

