# -*- coding: utf-8 -*-
"""
Exercise 8: Simple Search

"""

#I make a variable to make a list of strings.
String_List=("Jake", "Zac", "Ian", "Ron", "Sam", "Dave")
Target="Sam" #And make a second variable to define the target string.

if Target in String_List:
    print(f"You have found '{Target}' in the string list.") #If the Target is in the String List, it will print that.
else:
    print(f"'{Target}' is not in the list.")
#And if not, it will print that Target variable is not in the list.
