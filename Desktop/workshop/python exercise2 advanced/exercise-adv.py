# Advanced Python Challenge: Exercise 02 Operators and Conditionals
# -------------------------------------------

# Overview:
# This exercise challenges your understanding of Python operators, conditionals, and input handling.
# Complete each section with the required logic, using good variable names and adding comments where necessary.

# -------------------------------------------
# Question 1: Multi-Step Arithmetic Operations
# -------------------------------------------

# Task:
# Use compound arithmetic operators to modify values of a, b, and c.
# Then calculate the square root of the sum of their squares.
# Tip: Use the ma# -------------------------------------------th module.

import math

# Start with some base values
a = 5
b = 10
c = 7

# TODO: Add 3 to a using +=
a = 5 
a = a + 3
# TODO: Multiply b by 2 using *=
b = 10
b = b * 2
# TODO: Modulo c by 4 using %=
c = 7 
c = c % 4

# TODO: Calculate the square root of (a^2 + b^2 + c^2)
square = math.sqrt(2)
# TODO: Print the final result rounded to 2 decimal places
print(round(square, 2))

# -------------------------------------------
# Question 2: Complex Conditional Evaluation
# -------------------------------------------

# Task:
# Ask the user to input three integers (x, y, z).
# Then evaluate and print whether:
# - x is even
# - y is positive
# - z is between 10 and 50
# Use logical operators to combine the conditions.

# Tip: Use and/or to join conditions.

# TODO: Input x, y, z
x = int(input("input an integer: "))
y = int(input("input an integer: "))
z = int(input("input an integer: "))
# TODO: Create conditions:
#   is_even = True if x is even
#   is_positive = True if y > 0
#   is_in_range = True if z between 10 and 50
if x == 0:
 print(True)
if y > 0:
 print(True)
if z >= 10 or z <= 50:
 print(True)
# TODO: Create final_condition = is_even and is_positive and is_in_range
final_condition = x == 0 and y > 0 and z >= 10 or z <= 50
print(True)
 
# TODO: Print final_condition
print(final_condition)

# -------------------------------------------
# Question 3: Grading with Adjustments
# -------------------------------------------

# Task:
# Ask the user for their base score, then apply:
# - bonus points (+5)
# - late penalty (-10)
# Final score must not exceed 100 or drop below 0.
# Then assign a grade.

# Tip: Use min() and max() to constrain the score.

# TODO: Input score from user
score = int(input("users score: "))
# TODO: Apply adjustments
adjustments = score + 5 - 10
# TODO: Clamp score between 0 and 100
c-score == score < 100 or score > 0

# TODO: Use if-elif-else to determine grade and print it
if c-score >= 90 or c-score <= 100:
 print("A")
elif c-score >= 80 or c-score < 90:
 print("B")
elif c-score >= 70 or c-score < 80:
 print("C")
elif c-score >= 60 or c-score < 70:
 print("D")
elif c-score >= 50 or c-score < 60:
 print("E")
else:
 print("F")
# -------------------------------------------
# Question 4: Advanced Calculator
# -------------------------------------------

# Task:
# Ask the user to input two numbers and an operation (+, -, *, /, %, **).
# Handle division/modulus by zero with error checking.
# Perform the operation and print the result.

# Tip: Use try-except and elif branches for each operation.

# TODO: Input num1, num2
num1 = int(input("input integer: "))
num2 = int(input("input integer: "))
# TODO: Input operation
operation = input("input operation: ")
# TODO: Match operation using if-elif
# TODO: Handle division/modulus by zero with try-except
answer = num1 == 0 or num2 == 0 
# TODO: Print result
print(answer)
