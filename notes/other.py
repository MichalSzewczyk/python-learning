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
