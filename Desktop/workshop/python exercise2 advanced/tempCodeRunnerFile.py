
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
adjustments = score +