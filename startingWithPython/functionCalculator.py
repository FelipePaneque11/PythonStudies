#Create a program that acts as a simple calculator. The calculator should allow users to perform addition, subtraction, multiplication, and division.
#The program will have:
#A global variable result to store the ongoing result of calculations.
#Functions for each arithmetic operation (add, subtract, multiply, divide), each taking in a single parameter number and updating the global result variable accordingly.
#A reset function to reset the result back to zero.

result = 0

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1/num2

print(add(2,2))