#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

while True:
    print("Enter Your Options:")
    print("Enter '+' for addition")
    print("Enter '-' for subtraction")
    print("Enter '*' for multiplication")
    print("Enter '/' for division")
    print("Enter 'Q' to end the program")

    user_input = input("Enter Your Option : ")

    if user_input == "Q":
        break
    elif user_input in ("+", "-", "*", "/"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_input == "+":
            print("Result:", add(num1, num2))
        elif user_input == "-":
            print("Result:", subtract(num1, num2))
        elif user_input == "*":
            print("Result:", multiply(num1, num2))
        elif user_input == "/":
            print("Result:", divide(num1, num2))
    else:
        print("Invalid input")


# In[ ]:




