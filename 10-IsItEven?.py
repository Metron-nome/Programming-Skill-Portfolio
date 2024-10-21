# -*- coding: utf-8 -*-
"""
Exercise 10: Is It Even?

"""
#I first define even_or_odd.
def Is_Even_or_Odd(num):
    if num % 2 == 0: #If the number the user inputs is divisble by 2, it is even.
        return f"{num} is an even number."
    else: #If not, it is odd.
        return f"{num} is an odd number."
"""
The return statements is usually used to return data of any type.
It passes the values back from the function.

The function here meaning: if num % 2 == 0
"""

def main():
    while True:
        try:
            User_Input_Number = int(input("Please enter a number: ")) #This is when the program asks to enter a number.
            break #This stops the while loop.
        except ValueError: #If the user inputs that's not a numerical value, it will give an error.
            print("Invalid input. Please enter a valid number.") 
    Result = Is_Even_or_Odd(User_Input_Number) #This will then call the even_or_odd when the user types a number.
    print(Result) #It will then print the result if the number is odd or even.

if __name__ == "__main__":
    main()
