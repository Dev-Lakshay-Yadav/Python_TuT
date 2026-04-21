# Count positive numbers
# number_of_inputs = int(input("Enter the number of inputs: "))
# positive_count = 0
# for i in range(number_of_inputs):
#     number = float(input("Enter a number: "))
#     if number > 0:
#         positive_count += 1
# print(f"The number of positive numbers is: {positive_count}")


# Sum of Even Numbers up to n
# n = int(input("Enter a positive integer: "))
# even_sum = 0
# for i in range(2, n + 1, 2):
#     even_sum += i 
# print(f"The sum of even numbers up to {n} is: {even_sum}")


# Multiplication Table skip 5th iteration
# number = int(input("Enter a number for multiplication table: "))
# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(f"{number} x {i} = {number * i}")


# Reverse a String
# input_string = input("Enter a string to reverse: ")
# reversed_string = ""

# for char in input_string:
#     reversed_string = char + reversed_string

# print(f"The reversed string is: {reversed_string}")


# First Non Repeated Character
# input_string = input("Enter a string: ")

# for char in input_string:
#     if input_string.count(char) == 1:
#         print(f"The first non-repeated character is: {char}")
#         break
# else:    print("No non-repeated character found.")


# Factorial of a Number
# n = int(input("Enter a positive integer: "))

# if n < 0:  
#     print("Please enter a non-negative integer.")
# elif n == 0 or n == 1:
#     factorial = 1
# else :  
#     factorial = 1
#     i=n
#     while i > 1:  
#         factorial *= i
#         i -= 1

# print(f"The factorial of the entered number is: {factorial}")


# Validate Input (input number between 1 and 10)
# while True:   
#     number = int(input("Enter a number between 1 and 10: "))
#     if 1 <= number <= 10:
#         print(f"You entered: {number}")
#         break
#     else:
#         print("Invalid input. Please try again.")


# Check if a Number is Prime
# n = int(input("Enter a positive integer: "))

# if n <= 1:
#     print(f"{n} is not a prime number.")
# else:
#     is_prime = True
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(f"{n} is a prime number.")
#     else:
#         print(f"{n} is not a prime number.")


# list uniqueness checker
# items = ["apple", "banana", "apple", "cherry", "banana"]

# unique_items = set()

# for item in items:
#     if item in unique_items:
#         print(f"{item} is duplicate.")
#         break
#     unique_items.add(item)

# print(unique_items)


# Exponetial Backoff
import time

wait_time = 1  # initial wait time in seconds
max_retries = 5
attempts = 0

while attempts < max_retries:
    print(f"Attempt {attempts + 1}: Trying to connect... and waiting for {wait_time} seconds before retrying.")
    time.sleep(wait_time)
    wait_time *= 2  
    attempts += 1