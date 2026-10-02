class Base(object):
    pass #Empty clas

class Child(Base):
    pass #Empty class

#Test code:
print(issubclass(Child , Base))
print(issubclass(Base, Child))

c = Child()
b = Base()

print(isinstance(b, Child))
print(isinstance(c, Child))
print(isinstance(c, Base))