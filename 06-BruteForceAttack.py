# -*- coding: utf-8 -*-
"""
Exercise 6: Brute Force Attack

"""

#I first make a variable to define the correct password which is '12345'
Correct_Password="12345"
#And then make a loop using 'while' and ask the user to input the correct password.
while True:
    Enter_Password=input("Please enter the correct password:")
    
    if Enter_Password == Correct_Password: #The if statement makes it so that if the user enters the correct password.
        print("Good job! That is the correct password.") #It will then print "Good job! That is the correct password."
        break
    else:
        print("That is incorrect. Please enter the correct password")
        #But if the user enters an incorrect password, it will print "That is incorrect. Please enter the correct password"
        #And the program will keep looping until users enters the correct password.
