# Class and instantiate the objects

# Define a new user-defined class
# class keyword
'''
class Employee:
    # DATA
    # Define variables or attributes or properties
    emp_id = 0
    emp_sal = 0.0
    emp_name = ""

    # BEHAVIOR
    # Define methods of class
    # self paramteer inside method suggests that this method can be only used with the current object
    # of the related class

    def emp_details(self):
        print(f"The employee id is: {self.emp_id}")
        print(f"The salary of employee is: {self.emp_sal}")
        print(f"The name of employee is: {self.emp_name}")
    
    def input_details(self):
        self.emp_id = int(input("Enter an employee id: "))
        self.emp_sal = float(input("Enter the salary of employee: "))
        self.emp_name = input("Enter the name of employee: ")

# out of the class
# instantiate the class or create the object of class

print("Creating first object......")
emp_obj1 = Employee()
emp_obj1.input_details()
print("THE DETAILS OF EMPLOYEE ARE:")
emp_obj1.emp_details()

print("Creating second object......")
emp_obj2 = Employee()
emp_obj2.input_details()
print("THE DETAILS OF EMPLOYEE ARE:")
emp_obj2.emp_details()

print("Creating third object......")
emp_obj3 = Employee()
emp_obj3.input_details()
print("THE DETAILS OF EMPLOYEE ARE:")
emp_obj3.emp_details()
'''
'''
class Employee:
    # DATA
    # define a constructor by __init__() to initialize an object and this constructor will be called everytime we create a new object itself
    # We do not call init() separately. It is self-called when an object is created.
    def __init__(self):
        self.emp_id = 0
        self.emp_sal = 0.0
        self.emp_name = ""
    
    # BEHAVIOR
    # Define methods of class
    # self paramteer inside method suggests that this method can be only used with the current object
    # of the related class

    def emp_details(self):
        print(f"The employee id is: {self.emp_id}")
        print(f"The salary of employee is: {self.emp_sal}")
        print(f"The name of employee is: {self.emp_name}")
    
    def input_details(self):
        self.emp_id = int(input("Enter an employee id: "))
        self.emp_sal = float(input("Enter the salary of employee: "))
        self.emp_name = input("Enter the name of employee: ")

# out of the class
# instantiate the class or create the object of class

print("Creating first object......")
emp_obj1 = Employee()
emp_obj1.input_details()
print("THE DETAILS OF EMPLOYEE ARE:")
emp_obj1.emp_details()

print("Creating second object......")
emp_obj2 = Employee()
emp_obj2.input_details()
print("THE DETAILS OF EMPLOYEE ARE:")
emp_obj2.emp_details()

print("Creating third object......")
emp_obj3 = Employee()
emp_obj3.input_details()
print("THE DETAILS OF EMPLOYEE ARE:")
emp_obj3.emp_details()
'''

class Employee:
    # DATA
    # define a constructor by __init__() to initialize an object and this constructor will be called everytime we create a new object itself
    # We do not call init() separately. It is self-called when an object is created.
    def __init__(self, id=1, sal=0.0, name="User"):
        self.emp_id = id
        self.emp_sal = sal
        self.emp_name = name
    
    # BEHAVIOR
    # Define methods of class
    # self paramteer inside method suggests that this method can be only used with the current object
    # of the related class

    def emp_details(self):
        print(f"The employee id is: {self.emp_id}")
        print(f"The salary of employee is: {self.emp_sal}")
        print(f"The name of employee is: {self.emp_name}")
    
    def input_details(self):
        self.emp_id = int(input("Enter an employee id: "))
        self.emp_sal = float(input("Enter the salary of employee: "))
        self.emp_name = input("Enter the name of employee: ")

# out of the class
# instantiate the class or create the object of class

print("Creating first object......")
emp_obj1 = Employee(1, 100, "User")
print("The initial detials are:")
emp_obj1.emp_details()
emp_obj1.input_details()
print("THE DETAILS OF EMPLOYEE ARE:")
emp_obj1.emp_details()

print("Creating second object......")
emp_obj2 = Employee()
print("The initial detials are:")
emp_obj2.emp_details()
emp_obj2.input_details()
print("THE DETAILS OF EMPLOYEE ARE:")
emp_obj2.emp_details()

print("Creating third object......")
emp_obj3 = Employee()
print("The initial detials are:")
emp_obj3.emp_details()
emp_obj3.input_details()
print("THE DETAILS OF EMPLOYEE ARE:")
emp_obj3.emp_details()
