# -*- coding: utf-8 -*-
"""
Exercise 4: Primitive Quiz
"""
"""
Advanced Requirements
"""    
#I start by making a dictionary of the correct answers of the questions of each capitals of european countries.
Correct_Answers={
    "What is the capital of France?":"paris",
    "What is the capital of the United Kingdom?":"london",
    "What is the capital of Sweden?":"stockholm",
    "What is the capital of Austria?":"vienna",
    "What is the capital of Norway?":"oslo",
    "What is the capital of Germany?":"berlin",
    "What is the capital of Hungary?":"budapest",
    "What is the capital of Croatia?":"zagreb",
    "What is the capital of Finland?":"helsinki",
    "What is the capital of Greece?":"athens"
    }
#I then define a starting score for the quiz.
Score=0

#For these lines, it defines a dictionary 'Correct_Answers' that maps each questions of their correct answers.
#For each question, it checks if the user's answer matches the correct answer from the dictionary.
for Question, Correct_Answer in Correct_Answers.items():
    User_Answer=input(Question+" ")
    if User_Answer.lower()==Correct_Answer: #If the user's answer matches the correct answer from the question,
        print("That's correct.")            #It will print "That's correct." and add one score.
        Score+=1
    else:
        print(f"That is incorrect. The correct answer is {Correct_Answer.capitalize()}.")
        Score-=0     #If the user's answer is wrong, it will minus a the user's score until it is 0.
print(f"\nYou scored {Score} out of {len(Correct_Answers)}")
#Once the quiz is done, I programmed a way to show the total score of the user.
"""
The len function is the total number of items in a container, for this code, the total number of items in the dictionary,
is 10 items in total, so the total score a user can get is a maximum of 10.
"""
