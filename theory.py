# Every variable is an object of a particular class in Python
# For example
l = [1,2,3,4,5]
# l is object of class 'list'
print(type(l))

a = 10
# a is object of class 'int'
print(type(a))

# PROCEDURAL ORIENTED PROGRAMMING LANGUAGE
# creates a step by step program that guides the application through a sequence of instructions. 
# Each instruction is executed in order.

# OBJECT ORIENTED PROGRAMMING LANGUAGE
# each program is made up of many entities called objects.
# necessarily not in sequence

# What is an Object?
# Basic run-time entities in an object-oriented system
# When a program is executed the objects interact by sending messages to one another
# They may represent a person, a place, a bank account, a table of data or any item that the program must handle
# Objects have two components: 
# 1. Data (i.e. attributes)
# 2. Behaviors (i.e. methods)

# difference between function and method

# len() -> it is not called with a class and object with dot operator
# hence, it is a function
# functions are generic, they need not be called with a specific object using dot operator

# append() -> it is called with a list object using dot operator
# hence, it is a method
# methods are called with a specific object.

# What is a class?
# Special data type which defines how to build a certain kind of object
# stores some data items that are shared by all the instances of this class
# INSTANCES: objects that are created which follow the definition given inside of the class
# Python doesn't use separate class interface definition as in some languages like Java

# Methods in Classes
# define a method in a class by including function definitions within the scope of the class block
# There must be a special first argument self

# Instantiating Objects with __init__()
# __init__ is the default constructor

# Data Abstraction
# concept of hiding the internal details and describing things in simple terms
# for example, a method that adds teo integers. The internal processing of the method is hidden from the outer world.
# There are many ways to achieve abstraction in object-oriented programming, such as encapsulation and inheritance

# Public, Protected and Private Data
# name -> Public
# _name -> Protected
# __name -> Private

