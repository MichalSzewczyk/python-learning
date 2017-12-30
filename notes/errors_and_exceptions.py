# Python gives the way of controlling execution flow when an error occurs - exceptions handling mechanism.
# In general it works in the same way as in the other popular programming languages, like Java:
# Once exception is thrown, there are removed method frames from execution stack until there will be
# first method, which will handle this exception. If no one will handle - all frames will be removed and
# program stops.

# Example code:
def get_int_from_input_and_square():
    result = int(input())
    print(result ** 2)


# It is easy to break this code - just pass value which has not int representation.
# Better way would be to handle that case:
def get_int_from_input_and_square_fixed():
    try:
        result = int(input())
        print(result ** 2)
    except ValueError:
        print('Illegal input - unable to parse int value.')


get_int_from_input_and_square_fixed()

# Ways of exception handling:
try:
    # Code that may throw exception
    pass
except ValueError:
    # handle exception
    pass
except NameError as e:
    # handle named exeption
    pass
except (AttributeError, ZeroDivisionError):
    # handle multiple not named errors
    pass
except:
    # handle all other errors
    pass

# Ways of exception raising:
# Raise without description
# raise NameError
# Raise with description:
# raise NameError('An error occured')

try:
    # raise NameError('Hey there!')
    pass
except NameError:
    print('Exception occurred!')
    # And the following code will rethrow an exception
    raise

# There is also a way to execute code from separated clause when
# exception is not raised:
try:
    pass
except ValueError:
    print('Caught!')
else:
    print('Run without exception!')

# There is also finally block. Finally will always be executed no meter if exception occurred or not
# It's a good place to release the resources, close connections etc
try:
    pass
except ValueError:
    pass
finally:
    print('Closing resources')


# Custom exceptions - it is also possible to declare own exceptions:
class CustomException(Exception):
    def __init__(self):
        print('Created!')