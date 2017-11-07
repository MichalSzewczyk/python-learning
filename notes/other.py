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