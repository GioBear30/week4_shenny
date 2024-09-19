# Advanced Problem Set: Delving Deeper with Numbers in Python --- Bell Ringer

#################### PROBLEM 1: Basic Arithmetic & Order of Operations ####################
# Task 1: Using the order of operations (PEMDAS/BODMAS), evaluate the following expression:
# 3 + 6 * (5 + 4) / 3 - 7. Print the result.
print("-1")
# Task 2: Calculate the remainder when 145 is divided by 12 using modulo and print the result.
task2 = float (145%12)
print(task2)
# Task 3: Raise 7 to the power of 3 and print the result.
task3 = float (7 ** 3)
print(task3)
#################### PROBLEM 2: Working with Functions ####################
# Task 4: Given a list of numbers:
numbers = [23, 89, 12, 54, 92, 65, 71, 13, 45]
# Use the max() and min() functions to find the highest and lowest number respectively.
task4 = max(numbers)
print(task4)
# Task 5: Round the number 12.5678 to 2 decimal places.
task5 = float(round(12.5678, 2))
print(task5)
# Task 6: Find the absolute value of -45.
task6 = abs(-45)
print(task6)
#################### PROBLEM 3: Advanced Math Functions ####################
from math import *

# Task 7: Using the math library, find the floor value of 15.7.
task7 = float(floor(15.7))
print(task7)
# Task 8: Find the ceiling value of 15.2.
task8 = ceil(15.2)
print(task8)
# Task 9: Calculate the square root of 625.
task9 = sqrt(425)
print(task9)
#################### PROBLEM 4: Problem Solving ####################
# Task 10: You are given two lists:
prices = [34.56, 45.78, 23.89, 12.34, 78.90]
quantities = [3, 5, 2, 4, 6]

# Calculate the total cost for each item (price multiplied by quantity).
# Then, find the average cost of all items after rounding it to 2 decimal places.
value1 = prices[0] * quantities[0]
value2 = prices[1] * quantities[1]
value3 = prices[2] * quantities[2]
value4 = prices[3] * quantities[3]
value5 = prices[4] * quantities[4]
print(f"{value1}, {value2}, {value3}, {value4}, {value5},")
#################### END OF ADVANCED PROBLEM SET  -- end Bell Ringer  ####################