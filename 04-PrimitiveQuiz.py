# -*- coding: utf-8 -*-
"""
Exercise 4: Primitive Quiz

"""
#I first define the correct answer of the question.
Correct_Answer="Paris"

User_Answer=input("What is the Capital of France?") #I then program that requires an input from the user's answer.

if User_Answer.lower()==Correct_Answer.lower(): 
    print("The answer is Paris.")
else:
    print("Your answer is incorrect.")
#I programmed that if the user's answer is correct, it will print "The answer is Paris."
#If it is incorrect it will print "Your answer is incorrect." 

#The use of the lower() function and == makes it so that the answer is case sensitive.
