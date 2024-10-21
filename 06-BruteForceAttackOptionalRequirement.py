# -*- coding: utf-8 -*-
"""
Exercise 6: Brute Force Attack

"""

"""
Optional Requirement
"""

#I make a variable to define the correct password.
Correct_Password="12345"
Max_Attempts=5 #I make a variable to define the maximum of attempts.
Number_Of_Attempts=0 #And then I make another variable for the base value of the amount of attempts the user has.

while Number_Of_Attempts < Max_Attempts: 
    Enter_Password=input("Please enter the correct password:")
    Number_Of_Attempts+=1
#During the while loop, if the user keeps inputting the incorrect password, their number of attempts will increase by 1.
    if Enter_Password == Correct_Password:
        print("Good job! That is the correct password.")
        break  #If the user entered the correct password, it will print "Good job! That is the correct password."
    else:
        Amount_Of_Attempts = Max_Attempts - Number_Of_Attempts
        print(f"That is incorrect. You have {Amount_Of_Attempts} attempts remaining.")
#But if the user enters an incorrect password, it will loop until it reaches the maximum of attempts the user has, which is 5.
#And tells the user how many remaining attempts they have before the loop stops.
        if Number_Of_Attempts==Max_Attempts:
            print("You have reached the maximum attempts of entering the password." 
                  "The authorities have been alerted to your presence.")
          #If the user reaches the maximum attempts to enter a password, it will print 
          #"You have reached the maximum attempts of entering the password." "The authorities have been alerted to your presence."
          