# methods with variable positional arguments
# can be declared in many ways. There isn't any restriction for order of arguments:
def method1(*args, arg):
    pass


def method2(arg, *args):
    pass


def method3(arg1, *args, arg2):
    pass


# it's not possible to have two variable arguments in single method declaration:
# def method4(*arg1, arg2, *arg3):
#     pass


# passing many arguments without the position one will rise error:
# method1('foo', 'bar', 'foobar')
# in order to supply the one after variable arguments it's necessary to
# pass keyword argument:
method1('foo', 'bar', arg='foobar')
# like in case of non-variable arguments - positional arguments
# cannot occur after keyword ones
# method1('foo', arg='foobar', 'bar')

# when positional argument occurs before variable one, there is no need
# to pass it as keyword:
method2('foo', 'bar', 'foobar')

# Pass foo as arg and bar as *args:
method1('bar', arg='foo')
method2('foo', 'bar')

# Pass foo as arg1, bar as arg2 foobar as args (the only way)
method3('foo', 'foobar', arg2='bar')


# Unpacking variable positional arguments:
def func1(*args):
    print(args)


# In this function func1 gets args as arguments where args is a tuple.
# As a consequence inside func1 there is tuple of tuples
def func2(*args):
    func1(args)


# this call will result with one level nested tuple
func2('foo')


# To avoid it, we have to unpack the tuple:
def func3(*args):
    func1(*args)


# this call will tesult with zero level nested tuple
func3('foo')


# like in case of variable positional arguments, variable keyword arguments needs to be
# unpacked before passing them to method:
def f1(**kwargs):
    print(kwargs)

# as a result we will receive dict of dicts
def f2(**kwargs):
    f1(arg1 = kwargs)


f2(arg1='foo')

# in order to avoid it, we have to unpack variables:

def f3(**kwargs):
    f1(**kwargs)

f3(arg1='foo')
