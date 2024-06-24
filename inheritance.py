# Syntax:
'''
class SubClassName(ParentClass1,[,Parentclass2, ...]):
    "Optional Class String"
'''

# Simple single inheritance-> Single Parent class and single child class
'''
class Parent:
    value = 10
    def parentfunc1(self):
        print("This is parent class method", self.value)
class Child(Parent):
    def childfunc1(self):
        print("This is child class method", self.value)
obj1 = Child()
obj1.childfunc1()
obj1.parentfunc1()
'''

# Variable and method Overriding
'''
class Parent:
    value = 10
    def parentfunc1(self):
        print("This is parent class method", self.value)
    def func(self):
        print("This is func() of parent class")
class Child(Parent):
    value = 20
    def childfunc1(self):
        print("This is child class method", self.value)
    def func(self):
        print("This is func() of child class")
obj1 = Child()
obj1.childfunc1()
obj1.parentfunc1()
obj1.func()
'''

'''
class Parent:
    value = 10
    def parentfunc1(self):
        print("This is parent class method", self.value)
class Child(Parent):
    childValue = 20
    def childfunc1(self):
        print("This is child class method", self.childValue)
obj1 = Child()
obj1.childfunc1()
obj1.parentfunc1()
obj2 = Parent()
'''
'''
class Parent:
    value = 10
    def parentfunc1(self):
        print("This is parent class method", Parent.value)
        # parent.value -> Create a temporary unnamed Parent obj that will call Parent value
class Child(Parent):
    value = 20
    def childfunc1(self):
        print("This is child class method", self.value)
obj1 = Child()
obj1.childfunc1()
obj1.parentfunc1()
obj2 = Parent()
'''
# Check for subclass and superclass and object checking
'''
print("Child is subclass of Parent:", issubclass(Child, Parent))
print("Parent is subclass of Child:", issubclass(Parent, Child))
print("Child is subclass of Child:", issubclass(Child, Child))
print("obj1 is Object of Child:", isinstance(obj1, Child))
print("obj1 is Object of Parent:", isinstance(obj1, Parent))
print("obj2 is Object of Child:", isinstance(obj2, Child))
print("obj2 is Object of Parent:", isinstance(obj2, Parent))
'''

# to Access Prent class constructor
# super() -> super keyword is used to cacess the parent class constructor, method and variables  
'''
class Parent:
    value = 10
    def __init__(self, num):
        self.value = num
        print("In parent class Constructor: the value is", Parent.value)
        print("The num argument is", self.value)
    def parentfunc1(self):
        print("This is parent class method", Parent.value)
        # parent.value -> Create a temporary unnamed Parent obj that will call Parent value
    def func(self):
        print("This is func() of parent class")
class Child(Parent):
    value = 20
    def __init__(self):
        print("Inside child class constructor")
        super().__init__(30) # this will call init of parent class
    def childfunc1(self):
        print("This is child class method", self.value)
    def func(self):
        print("This is func() of child class")
        super().func() # this will call func() of parent class
obj1 = Child()
obj1.childfunc1()
obj1.parentfunc1()
obj1.func()
'''


# -------------------------------------------------------------------------------------------------#
# In Python, the order of resolving the call to constructprs and methods of inherited class
# MRO -> Method resolution order
'''
class Parent1:
    def __init__(self):
        print("Inside Parent class Constructor")
class Child1(Parent1):
    def __init__(self):
        print("Inside Child class constructor")
        super().__init__()
obj1 = Child1()
'''

# 2. Multiple Inheritance
# 2 or more parent class and only 1 child class
#         Parent1, Parent2, Parent3, ....ParentN
#            \       |       /           /
#              Inherited by 1 Child Class
'''
class Parent1:
    def __init__(self):
        print("Inside Parent 1 class Constructor")
        super().__init__()
class Parent2:
    # def __init__(self):
    #     print("Inside Parent2 class constructor")
    print("Inside parent2 class")
class Child(Parent1, Parent2):
    def __init__(self):
        print("Inside child contructor")
        super().__init__()
obj1 = Child()
print(Child.mro())
'''
'''
class Parent1:
    def __init__(self):
        print("Inside Parent 1 class Constructor")
        
class Parent2:
    def __init__(self):
        print("Inside Parent2 class constructor")
        super().__init__()
class Child(Parent2, Parent1):
    def __init__(self):
        print("Inside child contructor")
        super().__init__()
obj1 = Child()
print(Child.mro())
'''

# Multi-Level Inheritance
# Grandparent
#      |
#    Parent1     Parent2
#         \         /
#           Child
'''
class GrandParent:
    def __init__(self):
        print("Inside GrandParent class Constructor")
        super().__init__()
class Parent1(GrandParent):
    def __init__(self):
        print("Inside Parent 1 class Constructor")
        super().__init__()
        
class Parent2:
    def __init__(self):
        print("Inside Parent2 class constructor")
        super().__init__()
class Child(Parent1, Parent2):
    def __init__(self):
        print("Inside child contructor")
        super().__init__()
obj1 = Child()
print(Child.mro())
'''

# Hierarchical Inheritance
#          Only 1 Parent Class
#      /      |        |         \
#   Child1  Child2   Child3 ...ChildN

'''class Parent1():
    def __init__(self):
        print("Inside Parent 1 class Constructor")

class Child1(Parent1):
    def __init__(self):
        print("Inside child 1 contructor")
        super().__init__()
class Child2(Parent1):
    def __init__(self):
        print("Inside child 2 contructor")
        super().__init__()
class Child3(Parent1):
    def __init__(self):
        print("Inside child 3 contructor")
        super().__init__()
print("......................Creating Child1 object..............................")
obj1 = Child1()
print("......................Creating Child2 object..............................")
obj2 = Child2()
print("......................Creating Child3 object..............................")
obj3 = Child3()
print("................................MRO.......................................")
print(Child1.mro())
print(Child2.mro())
print(Child3.mro())
'''
# Diamond Problem - combination of multiple and multi-level inheritance
#             GrandParent
#             /          \
#          Parent1      Parent2
#             \          /
#              Child Class
'''
class GrandParent:
    def func1(self):
        print("Inside GrandParent func1()")
class Parent1(GrandParent):
    def func1(self):
        print("Inside Parent 1 func1()")
        super().func1()
class Parent2(GrandParent):
    def func1(self):
        print("Inside Parent 2 func1()")
        super().func1()
class Child(Parent1, Parent2):
    pass

obj1 = Child()
obj1.func1()
print(Child.mro())'''