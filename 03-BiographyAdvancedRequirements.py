# -*- coding: utf-8 -*-
"""
Exercise 3: Biography
"""

"""
Advanced Requirements
"""

User_Info=input("What is your name?")
User_Hometown=input("Where do you live?")

while True:
    try:
        User_Age=int(input("How old are you?"))
        break
    except ValueError:
        print("Please enter a valid number.")
        
print(f"Name: {User_Info} Hometown:{User_Hometown} Age:{User_Age}.")

"""
Full Explanation:

    For Line 27, and 28, I coded it in a way that needed the user's name and hometown.
    However for the age, if the user already typed their name and hometown, it will then
    ask for their age, but if they typed anything else than a numerical value.
    
    It will print("Please enter a valid number.") and give an error.
    If the user inputs a numerical value in when it asks for the user's age,
    It will print(f"Name:{User_Info},Hometown:{User_Hometown},Age:{User_Age}") instead.

"""