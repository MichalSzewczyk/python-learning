# It's possible to write object oriented code in python.
# name          - reference to the object
# namespace     - associative mapping of names to the objects
# attribute     - name following a dot: sth.<attribute_name>


# Syntax of class definition:
class Example:
    # Assignments and function definitions goes here
    # ...
    any_attribute = 10

    def any_function(self):
        pass

    pass


# Class definition introduces new namespace
# In fact all class members are placed in __dict__ attribute
print(Example.__dict__)


# Class definition creates an object representing type, for example int, str
# Class definition creates an object of type of this class but doesn't instantiate the class.
# In order to instantiate the class it is necessary to call the constructor
class DefinitionExample:
    # Class attribute
    any_attribute = 10

    # Methods (even non static) are also class attributes:
    def any_method(self):
        pass


# Type object
# Type object gives possibility to instantiate objects and access class level attributes:
print(DefinitionExample)
# Instantiate
instance = DefinitionExample()
# Access class member attributes:
print(DefinitionExample.any_attribute)
print(DefinitionExample.any_method)

# Class instantiation
example = DefinitionExample()
print(example)


# Custom constructor with default arguments:
class Complex:
    def __init__(self, real_part=0, imag_part=0):
        self.real_part = real_part
        self.imag_part = imag_part

    def __str__(self):
        return 'Complex number: ({}, {})'.format(self.real_part, self.imag_part)


complex = Complex(10, 10)
print(complex)


# Attributes resolution:
# First python searches in object attributes, later in class attributes:
class Test:
    any_attribute = 10

    def __init__(self):
        self.any_attribute = 20


test = Test()
# The following code will print value of object level attribute
print(test.any_attribute)
# delete object attribute
del test.any_attribute
# The following code will print value of class level attribute
print(test.any_attribute)
del Test.any_attribute
# And the following will rise Exception:
# print(test.any_attribute)

# It is possible to set attributes for objects and classes on the fly:
test.any_not_existent_attribute = 100
print(test.any_not_existent_attribute)
# attributes inserted on the fly also are added to __dict__ attribute.
print(test.__dict__)


# Methods vs Functions in python:
class Test:
    def any_function(self):
        print('hello!')


test = Test()
# The following is function - in order to call it it is necessary to pass an instance of Test class
print(Test.any_function)
# The following is method - it's already bounded to the object test
print(test.any_function)
# Function call:
Test.any_function(test)
# Method call:
test.any_function()


# Method = obejct + function
# When invoking method, actually there is function invoked with first argument - object
# on which the function was called
# test.any_function() = Test.any_function(test)
# But it's impossible to pass the 'self' argument to method. The following code will rise TypeError:
# test.any_function(test)



# In python there is no way to make the class member private.
# Clients can modify anything.


# Code style conventions:
# 1. Method's first parameter should be 'self'
# 2. To inform client that the class member should not be used, we add '_' before the attribute name
# 3. Verbs for methods, nouns for data attributes


# Inheritance:
# To make class inheritance we add the base class into the brackets:
class Base:
    pass


class Derived(Base):
    pass


# Since Python 3 classes inherits from Object class.
# Class members lookup begins in the most derived class and goes up through inheritance hierarchy
# It's possible to override methods from the base classes

# In python there is support for multiple inheritance:
class Base1:
    def method(self):
        print('base1')


class Base3:
    def method(self):
        print('base2')


class Base2:
    def method(self):
        print('base3')


class MultiDerived(Base1, Base2, Base3):
    pass


# In case of multiple inheritance, attributes are looked up in the following order:
# - up in the inheritance hierarchy
# - from left to right on the same level of inheritance

multi_derived = MultiDerived()
multi_derived.method()

# So previous invocation will print 'base1'

# In order to print all classes from which class is derived and this class, we have to use method: mro
print(MultiDerived.mro())

