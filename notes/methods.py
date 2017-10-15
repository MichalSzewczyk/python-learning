# example function definition
def sample_function(arg1: str, arg2):
    print(arg1 + arg2)
    return True


# ways of method invocation:
# 1. normal
sample_function('foo', 'bar')

# 2. with other argument order
sample_function(arg2='foo', arg1='bar')


# default argument values
def any_function(arg1='foo', arg2='bar'):
    pass
