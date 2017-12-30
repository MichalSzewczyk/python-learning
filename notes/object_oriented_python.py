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
del test.any_attribute
# And the following will rise Exception:
# print(test.any_attribute)

