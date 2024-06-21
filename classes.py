class Sample:
    # public variable
    var1 = "Public Variable"
    # protected variable
    _var2 = "Protected Variable"
    # private variable
    __var3 = "Private Variable"

    def __init__(self):
        self.var1 = "Public variable in constructor"
        self._var2 = "Protected variable in constructor"
        self.__var3 = "Private variable in constructor"
    def display(self):
        print("The public variable is:", self.var1)
        print("The protected variable is:", self._var2)
        print("The private variable is:", self.__var3)

samp_obj = Sample() 
samp_obj.display()
print()
print("The intial value of public variable:",samp_obj.var1)
samp_obj.var1 = "new value outside"
print("The updated value of public variable:",samp_obj.var1)
print()
print("The intial value of protected variable:",samp_obj._var2)
samp_obj._var2 = "New value of protected variable"
print("The updated value of protected variable:",samp_obj._var2)
print()
# print(samp_obj.__var3) # Error, private variable
samp_obj.display() # it will display the value of private variable also

# public and privae variables work same for one class and different for multiple classes in case of INHERITANCE
