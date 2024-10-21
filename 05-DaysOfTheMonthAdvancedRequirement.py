# -*- coding: utf-8 -*-
"""
Exercise: Days Of The Month
"""
"""
Advanced Requirement
"""
#I first code a dictionary, Month:Days of Month.
Day_Months={
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
   10: 31,
   11: 30,
   12: 31
   }

Month=int(input("Please enter a month number.(1-12)"))
#After that, in line 52, I ask the user's input to enter a month number. (1-12)
if Month in Day_Months:
    print(f"There are {Day_Months[Month]} days in a month ({Month}).")
if Month == 2: #If the user's input is the 2nd month, the program will first ask if the year is a leap year.
    Leap_Year=input("Is this year a leap year? (Yes/No):")
    if Leap_Year.lower()=="Yes": #If the user's answer is Yes, then it will print "There are 20 days inFebruary."
       print("There are 20 days in February.")
    else:
       print("There are 28 days in February.") #If the user's answer is No then it will print "There are 28 days in February."
else:
    print("Invalid month number. Please type a month number.(1-12).")
#If the user inputs an invalid value, it will then print an invalid month number message.
