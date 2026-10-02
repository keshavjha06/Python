class Employee:

    #hidden data member of Employee class
    __salary = 1000

e1 = Employee()
#print(e1.__salary) - this is not accessible because it is a private member of the class

#access the private member using name mangling
print(e1._Employee__salary)