# Assignment- 7 of this Python Course.

"""

***** Questions On – list, Tuple and its functions  *****

    Questions:

        1-> Write a python script to store seven fruits name in a list entered by the user and display that list.
        2-> Write a python script to accept marks of 6 students and display them in a sorted manner.
        3-> Write a python script to Check that a tuple cannot be changed in python.
        4-> Write a python script to sum a list with 4 numbers.
        5-> Write a python script to count the number of zeros(0) in the following tuple.
            -> like:- tp = (7, 0, 9, 0, 0, 10, 8)

    Answers:

        => All the answers are out of the Comment box.


"""

print("Assignment- 7 of this Python Course.\n")

# Answer-1:
print("Solution of question-1")

fruitsList = [
            input("Enter 1st Fruit name : "),
            input("Enter 2nd Fruit name : "),
            input("Enter 3rd Fruit name : "),
            input("Enter 4th Fruit name : "),
            input("Enter 5th Fruit name : "),
            input("Enter 6th Fruit name : "),
            input("Enter 7th Fruit name : ")
            ]
print(fruitsList, "\n")

# Answer-2:
print("\nSolution of question-2")

marksList = [98, 96, 99, 94, 87, 92]
marksList.sort()
print("The marks of 6 Students are : ", marksList, "\n")

# Answer-3:
print("Solution of question-3", "\n")

# Answer-4:
print("Solution of question-4")

numbersList = [4, 10, 20, 6]
sum= numbersList[0]+ numbersList[1]+ numbersList[2]+ numbersList[3]
print("The sum of list with 4 Numbers is : ", sum, "\n")

# Answer-5:
print("Solution of question-5")

tp = (7, 0, 9, 0, 0, 10, 8)
print("The count of 0 in the Tuple is : ", tp.count(0), "\n")
