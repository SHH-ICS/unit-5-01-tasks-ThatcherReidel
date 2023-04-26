# Create a program that accepts 2 numbers from the user. 
# Your program will output a random number between the range given by the user.
import random

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    num1, num2 = num2, num1

random_num = random.randint(num1, num2)

print("Random number between", num1, "and", num2, "is:", random_num)
