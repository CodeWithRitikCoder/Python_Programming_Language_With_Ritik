# Assignment- 5 of this Python Course.

"""

***** Questions On – String and its functions *****

    Questions:

        1-> Write a python script to display a user entered name followed by Good Afternoon using input() function.
        2-> Write a python script to fill in a letter template given below with name and data.
            letter= '''Dear <|NAME|>
                            You are Selected!
                                <|DATE|>'''
        3-> Write a python script to delete double spaces in a string.
        4-> Replace the double spaces from Problem-3 with single spaces.
        5-> Write a python script to format the following string words in letter form as shown in question-2 using
            escape sequence characters.
            "Dear Ritik, You are selected for the Software Engineering Role at MicroSoft! Thanks."

    Answers:

        => All the answers are out of the Comment box.


"""

print("Assignment- 6 of this Python Course.\n")

# Answer-1:
print("Solution of question-1")
# name = input("Enter your name here : ")
# print("Good Afternoon : ", name)

# Answer-2:
print("\nSolution of question-2")
letter = '''Dear Ritik
    You are selected for the 
    Software Engineering Role at MicroSoft!
        30/11/2023'''
print(letter,"\n")

# Answer-3:
print("Solution of question-3")
myString1 = "My  Name  Is  Ritik"
print(myString1)
print(myString1.replace("  ", ""), "\n")

# Answer-4:
print("Solution of question-4")
myString1 = "My  Name  Is  Ritik"
print(myString1)
print(myString1.replace("  ", " "), "\n")

# Answer-5:
print("Solution of question-5")
print("Dear Ritik, \n\tYou are selected for the \n\tSoftware Engineering Role at MicroSoft! \n\t\tThanks.")
