# -*- coding: utf-8 -*-
"""
Exercise 5: Days Of The Month

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

#After that, in line 24, I ask the user's input to enter a month number. (1-12)
Month=int(input("Please enter a month number.(1-12)"))

#If any of the user's input is in the dictionary, it will print the number of days of the user's selected number of month.
if Month in Day_Months:
    print(f"There are {Day_Months[Month]} days in a month ({Month}).")
else:
   print("Invalid month number. Please type a month number.(1-12).")    
#And if the user inputs an invalid value, it will then print an invalid month number message.
