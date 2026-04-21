# calculate the square of a number
# def square(x):
#     return x * x

# result = square(5)
# print(result)


# function with multiple parameters
# def add(a, b):
#     return a + b

# result = add(3, 4)
# print(result)


# polymorphism in functions
# def multiply(a, b):
#     return a * b

# print(multiply(2, 3))
# print(multiply("a", 5))
# print(multiply(5, 'a'))


# function return both area and circumference of a circle
# import math

# def circle_properties(radius):
#     area = math.pi * radius ** 2
#     circumference = 2 * math.pi * radius
#     return area, circumference

# area, circumference = circle_properties(5)
# print(f"Area: {area}")
# print(f"Circumference: {circumference}")


# function with default parameters
# def greet(name, greeting="Hello"):
#     return f"{greeting}, {name}!"  

# print(greet("Alice"))
# print(greet("Bob", "Hi"))


# lambda function to calculate the cube of a number
# cube = lambda x: x ** 3 
# print(cube(3))  # Output: 27


# function with *args to calculate the sum of all numbers
# def sum_all(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total

# result = sum_all(1, 2, 3, 4, 5)
# print(result)  # Output: 15


# function with **kwargs to print user information
# def print_user_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_user_info(name="Alice", age=30, city="New York")


# generator function with yield even numbers up to a given limit
# def even_numbers(limit):
#     for num in range(limit):
#         if num % 2 == 0:
#             yield num

# for even in even_numbers(10):
#     print(even)  


# Recursive function to calculate the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print(result)  # Output: 120