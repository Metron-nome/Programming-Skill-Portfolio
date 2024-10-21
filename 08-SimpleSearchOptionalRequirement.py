# -*- coding: utf-8 -*-
"""
Exercise 8: Simple Search

"""

"""
Optional Requirement
"""

#I make a variable to make a list of strings.
String_List=("Jake", "Zac", "Ian", "Ron", "Sam", "Dave")
String_Target="Sam" #And make a second variable to define the target string.

User_Input_Target=input("Please enter a name to search for:")
#The program then asks the user to input a name to search for in the string list.
if User_Input_Target in String_List:
    print(f"You have found '{User_Input_Target}' in the string list.")
#If the user user inputs any of the name in the string list, it will print the name found in the list.
#It is case sensitive.

if User_Input_Target not in String_List:
        print(f"'{User_Input_Target}' is not in the list.")
#If the user entered a name that is not in the string list, the program will let the user know that name is not in the list.