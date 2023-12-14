# List and List Functions in Python.

# What is List in Python.
"""
=> What is List in Python?
    -> Python lists are containers to store a set of values of any data type.
    -> python lists are Mutable -> It means list can change.
    -> and list can store value of any data type.
        like:- friends = ["Vishu", "Vikas", 12, 34.5, False]

=> List indexing.
    -> A list can be indexed just like a string.
        list1 = [7, 9, "Ritik"]

        list1[0] ==> 7
        list1[1] ==> 9
        list1[76] ==> Error
        list1[1:2] ==> [7, 9]  ==> List slicing.
        list1[0:] ==> [7, 9, 'Ritik']

=> List functions.
    -> Consider the following list:
        like:- list1 = [1, 8, 7, 2, 21, 15]

    1-> list1.sort() ==> This function will Updates the list to this -->[1, 2, 7, 8, 15, 21] in Sorting Order
    2-> list1.reverse() ==> This function will Updates the list to this -->[15, 21, 2, 7, 8, 1] in Reverse Order
    3-> list1.append(8) ==> This function will add 8 at the end of the list. --> [1, 8, 7, 2, 21, 15, 8] like this.
    4-> list1.insert(3, 9) ==> This function will add 9 at 3rd index of the list. --> [1, 8, 7, 9, 2, 21, 15, 8] like
        this.
    5-> list1.pop() ==> This function will delete last element from the list and return its value.
    6-> list1.pop(2) ==> This function will delete element at index 2 from the list and return its value.
    7-> list1.remove(21) ==> This function will remove 21 from the list.
    8-> len(list1) ==> This function will return length of the list.
    9-> min(list1) ==> This function will return min value of the list.
    10-> max(list1) ==> This function will return max value of the list.


"""
# Practice on List
print("Practice on List")
list1 = [7, 9, "Ritik"]
print(list1)
print(type(list1))

numbers = [2, 4, 8, 29, 23]
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4], "\n")

# Practice on List Slicing.
print("Practice on List slicing")
print(numbers[1:4])
print(numbers[1:])
print(numbers[:4])
print(numbers[:])
print(numbers[1:3:2])
print(numbers[::-1], "\n")

# Practice on List functions. and in most cases all the functions of list will change the original list.
print("Practice on List functions")
list2 = [1, 8, 7, 2, 21, 15]
print("Its my list2 : ", list2)

list2.sort()
print("This is my Sorted list2 : ", list2)

list2.reverse()
# print("This is my reversed list2 : ", list2.reverse()) # => We can't use this function like this.
print("This is my reversed list2 : ", list2)

list2.append(23)
print("Now the list2 is : ", list2)

list2.insert(3, 24)
print("Now the list2 is : ", list2)

list2.pop()
print("After pop - now the list2 is : ", list2)

list2.pop(2)
print("After pop(2nd index value) - now the list2 is : ", list2)
print("After pop(3rd index value) - from the list which is : ", list2.pop(3))

list2.remove(24)
print("After remove(26) - now the list2 is : ", list2)

print("The length of the list2 is : ", len(list2))

print("The min value of the list2 is : ", min(list2))

print("The max value of the list2 is : ", max(list2))


