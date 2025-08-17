# This program performs basic arithmetic operations on two user-input numbers.

# Part 1: Addition and Subtraction

# Prompt the user for the first number and convert the input to an integer.
num1 = int(input("Enter the first number: "))

# Prompt the user for the second number and convert the input to an integer.
num2 = int(input("Enter the second number: "))

# Calculate the sum and print the result.
addition_result = num1 + num2
print("The sum of", num1, "and", num2, "is:", addition_result)

# Calculate the difference and print the result.
subtraction_result = num1 - num2
print("The difference between", num1, "and", num2, "is:", subtraction_result)

# --- End of Part 1 ---

# Part 2: Multiplication and Division

# Prompt the user for a new set of numbers for Part 2.
# You can use the same variables or new ones. 
print("\n--- Part 2: Multiplication and Division ---")

# Prompt the user for the first number and convert the input to an integer.
num1 = int(input("Enter the first number: "))

# Prompt the user for the second number and convert the input to an integer.
num2 = int(input("Enter the second number: "))

# Calculate the product and print the result.
multiplication_result = num1 * num2
print("The product of", num1, "and", num2, "is:", multiplication_result)

# Calculate the division and print the result.
# Use float() to ensure a precise decimal result.
division_result = num1 / num2
print("The division of", num1, "by", num2, "is:", division_result)

# --- End of Part 2 ---
