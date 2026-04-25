
# Scopes

# x = 99

# def func():
#     print(x)

# print(x)

# def func2():
#     x = 88
#     print(x)

# def func3():
#     global x
#     x = 77
#     print(x)

# func()
# func2()
# func3()

# print(x)


# Closures
# def outer():
#     x = 99
#     def inner():
#         print(x)
#     return inner

# result = outer()   # inner function is returned and assigned to result variable
# result()   # when we call result(), it executes the inner function, which has access to the variable x defined in the outer function's scope. Therefore, it prints 99.


def outer2(num):
    def inner2(x):
        return x ** num
    return inner2

square = outer2(2)  # square is assigned the inner function with num set to 2
cube = outer2(3)    # cube is assigned the inner function with num set to 3

print(outer2(4)(5))  # when we call outer2(4)(5), it first calls outer2 with num set to 4, which returns the inner function. Then, it immediately calls the returned inner function with x set to 5. Therefore, it calculates 5 raised to the power of 4 and prints 625.

print(square(5))  # when we call square(5), it executes the inner function, which has access to the variable num defined in the outer function's scope. Therefore, it calculates 5 raised to the power of 2 and prints 25.
print(cube(5))    # when we call cube(5), it executes the inner function, which has access to the variable num defined in the outer function's scope. Therefore, it calculates 5 raised to the power of 3 and prints 125.
