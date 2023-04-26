# Create a program that will ask the user an addition question. 
# The program will generate two random numbers between 1 and 100, and display them as an addition question with appropriate prompts.
import random

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)

answer = num1 + num2

user_answer = int(input("What is " + str(num1) + " + " + str(num2) + "? "))

if user_answer == answer:
    print("Correct!")
else:
    print("Incorrect. The answer is " + str(answer))