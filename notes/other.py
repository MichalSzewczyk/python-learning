def get_type_of(*args):
    print(type(args))


get_type_of()


# It is possible to dynamically add methods to objects of class:
class Foo:
    def __init__(self):
        pass


foo_object = Foo()


def bar_method():
    print('Executing bar method.')


foo_object.method = bar_method

foo_object.method()


# As a consequence of fact that functions are objects in python, we can dynamically add function to function object:

def foo():
    print('foo function')


def bar():
    print('bar function')


foo.bar = bar

foo()
foo.bar()


# So indicates fact that we can create stateful decorators with functions to modify their state:

class decorator:
    def __init__(self, fn):
        self.fn = fn
        self.fn.cache_reset = self.cache_reset

    def __call__(self, *args, **kwargs):
        self.fn(*args, **kwargs)

    def cache_reset(self):
        print('success!')


@decorator
def test():
    print('test')


test()
test.cache_reset()

# what is false in python
# None
print(bool(None) == False)
# zero
print(bool(0) == False)
print(bool(0.0) == False)
# empty string
print(bool('') == False)
# empty collection
print(bool([]) == False)

# So as a consequence of fact that empty collection is false, we can easily do the check if collection is empty:
d = {}
if d:
    print('Not empty')
else:
    print('Empty')

# sort list:
any_list = [3, 4, 2, 1, 2]
any_list.sort()

# sort set:
any_set = {3, 1, 2, 4}
sorted(any_set)

dictionary = {'foo': 1, 'bar': 2}
sorted(dictionary.items(), key=lambda x: x[0])

# eval(string) - executes passed string as it is python command:
eval('print(\'test\')')
# repr(value) - returns string representation of passed object:
print(repr([1, 2, 3]))
# char to ascii conversion:
print(ord('a'))

# ascii to char convertion:
# print(unichr(97))

# convert int to hexadecimal system string representation:
print(hex(15))

# convert int to hexadecimal system string representation:
print(hex(15))

# convert int to octal system string representation:
print(oct(15))

# get an absolute value:
print(abs(-2))

print(all([True, False]))

print(any([True, False]))

print(bin(10))

print(bool(0))

print(bytearray([1, 2, 3, 4]))

print(chr(97))

# print(cmp(1,2))

print(complex(10))

dict(key='')

print(dir())

print(divmod(1, 2))

for i in enumerate([1, 2, 3, 4, 5], 4):
    print(i)

s = frozenset([1, 2, 3, 4, 5])
dictionary = {s: ''}

print(globals())

print(hash('asd'))

help('str')

print(id('foo'))

print(isinstance(10, int))

print(max(1, 2, 3))

print(ord('a'))
print(ord('a'))

print(pow(2, 3))


@property
def foo():
    pass


# foo.__setattr__('asd', lambda x: print(x))
# print(foo.asd('test'))


print(repr('asd'))

print(round(1.234, 3))

print([1, 2, 3, 4, ][slice(12)])

print(sorted({2: 3, 1: 2}))
