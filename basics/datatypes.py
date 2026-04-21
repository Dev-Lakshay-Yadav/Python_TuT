# object types or data types

# numbers - int (1,2,3,4), float (2.5), complex (1+2j)
# strings - "Hello", 'World', '''Python''', """Programming""", b"Byte string", u"Unicode string"
# boolean - True, False
# none - None

# list - [1, 2, 3], ["a", ["b", "c"]], [1, "a", True] continuous memory allocation, mutable
# tuple - (1, 2, 3), ("a", "b", " c"), (1, "a", True) continuous memory allocation, immutable
# dict - {"name": "Alice", "age": 30}, {"name": "Bob", "age": 25} key-value pairs, mutable

# set - {1, 2, 3}, {"a", "b", "c"}, {1, "a", True} unordered collection of unique elements, mutable
# frozenset - frozenset({1, 2, 3}), frozenset({"a", "b", "c"}), frozenset({1, "a", True}) unordered collection of unique elements, immutable

# file - open("file.txt", "r"), open("file.txt", "w") used for reading and writing files, mutable

# function - def func(): pass, lambda x: x + 1 used for defining functions, mutable
# module - import math, import os used for importing modules, mutable
# class - class MyClass: pass used for defining classes, mutable

# advanced data types
# list comprehension - [x for x in range(10)], [x**2 for x in range(10)] used for creating lists, mutable
# decorator - @decorator used for modifying functions or classes, mutable
# generator expression - (x for x in range(10)), (x**2 for x in range(10)) used for creating generators, mutable
# iterator - iter([1, 2, 3]), iter("Hello") used for creating iterators, mutable
# lambda function - lambda x: x + 1, lambda x, y: x + y used for creating anonymous functions, mutable
# meta programming - type("MyClass", (object,), {"attr": "value"}) used for creating classes dynamically, mutable