import timeit
from functools import reduce
from itertools import chain


def flow_rate(weight, time, period=60, units_per_kg=1000):
    """ Funkcja wylicza ile wagi produktu przybyło/ubyło w jednostce czasu """
    return weight * units_per_kg / time * period


weight = 0.5
time = 3

flow = flow_rate(weight, time, period=60, units_per_kg=1000)
print("{} grams per minute".format(flow))

flow = flow_rate(weight, time, period=1, units_per_kg=1)
print("{0:.3} kg per second".format(flow))

flow = flow_rate(weight, time)
print("{0:.3} grams per minute".format(flow))

try:
    flow = flow_rate(weight, time, 3600, 2.2)
except TypeError:
    print(True)


def time(func):
    """ Wypisuje czas wywołania udekorowanej funckji """

    def decorate(*args, **kwargs):
        start = timeit.default_timer()
        result = func(*args, **kwargs)
        exec_time = timeit.default_timer() - start
        print('Function {} took: {} seconds.'.format(func.__name__, exec_time))
        return result

    return decorate


@time
def squares_list(n):
    squares = []
    for i in range(n):
        squares.append(i ** 2)
    return squares


@time
def squares_comprehension(n):
    return [i ** 2 for i in range(n)]


@time
def squares_map(n):
    return map(lambda x: x ** 2, range(n))


n = 1000000
l = squares_list(n)
c = squares_comprehension(n)
m = squares_map(n)

import sys

sys.float_info.epsilon  # epsilon maszynowy


def derivate(epsilon=None):
    """
   Zwraca pochodną funkcji w punkcie, wg. wzoru f'(x) = [f(x+h) - f(x)]/h,
   gdzie h jest parametrem dekoratora, jeśli nie zostanie podany, należy przyjąć 1000 * epsilon maszynowy
   """
    if epsilon is None:
        epsilon = 1000 * sys.float_info.epsilon

    def decorator(fn):
        def decorate(x):
            return (fn(x + epsilon) - fn(x)) / epsilon

        return decorate

    return decorator


@derivate(0.01)
def f(x):
    return x * x


@derivate(0.00001)
def g(x):
    return x * x * x + 3


def test(a, b, eps=1):
    return abs(round(a) - round(b)) < eps


print(test(f(100), 200.0))
print(round(f(0)) == 0.0)

print(test(g(100), 30000.0))
print(round(g(0)) == 0.0)

from random import random

for x in [random() * 1000. for _ in range(20)]:
    print(f(x), 2 * x, '\t', test(f(x), 2 * x))
    print(g(x), 3 * x ** 2, '\t', test(g(x), 3 * x ** 2))


def accepts(*types):
    """Sprawdza czy udekorowanej funckji zostały podane odpowiednie parametry zdefiniowane
       w argumentach dekoratora"""

    def decorator(fn):
        def decorate(*args, **kwargs):
            for x in filter(lambda t: type(t[1]) is not t[0], zip(types, chain(args, kwargs.values()))):
                raise TypeError('Arguments not matched: {} - {}'.format(x[0], x[1]))
            return fn(*args, **kwargs)

        return decorate

    return decorator


@accepts(str)
def capitalize(word):
    return word[0].upper() + word[1:]


print(capitalize('ola') == 'Ola')

try:
    capitalize(2)
except TypeError:
    print(True)


@accepts(float, int)
def static_pow(base, exp):
    return base ** exp


print(static_pow(2., 2) == 4.)
print(static_pow(2., exp=2) == 4.)
print(static_pow(base=2., exp=2) == 4.)

try:
    static_pow('x', 10)
except TypeError:
    print(True)

try:
    static_pow(2, 2.2)
except TypeError:
    print(True)


def returns(*types):
    """Sprawdza czy udekorowana funkcja zwraca poprawne argumenty, zdefiniowane w parametrach dekoratora"""

    def decorator(fn):
        def decorating(*args, **kwargs):
            result = fn(*args, **kwargs)
            filter(lambda t: type(t[0]) == t[1], zip(result, types))
            return result

        return decorating

    return decorator


@returns(str)
def str_only_identity(word):
    return word


print(str_only_identity('hello') == 'hello')

try:
    str_only_identity(10)
except TypeError:
    print(True)


@returns(int, int)
def split_indices(x):
    return x[0], x[1]


print(split_indices(x=[6, 9]) == (6, 9))

try:
    split_indices('AB')
except TypeError:
    print(True)

from random import random


class cached:
    def __init__(self, fn):
        self.fn = fn
        self.fn.cache_reset = self.cache_reset
        self.dictionary = {}

        self.evaluation_counter = 0
        self.execution_counter = 0
        self.fn.cache_status = self.cache_status

    def __call__(self, *args, **kwargs):
        self.execution_counter += 1
        args_code = ''
        for i in args:
            args_code += str(i)

        reduced_args = reduce(lambda l, r: l + r, sorted(map(lambda v: str(v), kwargs)), '')
        args_code += reduced_args
        if args_code in self.dictionary.keys():
            result = self.dictionary[args_code]
        else:
            result = self.fn(*args, **kwargs)
            self.dictionary[args_code] = result
            self.evaluation_counter += 1
        return result

    def cache_reset(self):
        self.dictionary.clear()

    def cache_status(self):
        return 'Function {} called {} times, evaluated {} times'.format(self.fn.__name__, self.execution_counter,
                                                                        self.evaluation_counter)


@cached
def foo(x, y=1, z=4):
    return random()


print(foo(3) == foo(3))
print(foo(4) == foo(4))
print(foo(3, z=-1, y=3) == foo(3, y=3, z=-1))
print(foo(3) != foo(x=3))
a = foo(3)
foo.cache_reset()
print(a != foo(3))
print(foo.cache_status() == 'Function foo called 10 times, evaluated 5 times')


def zlozenie(n):
    def decorator(fn):
        def decorating(*args, **kwargs):
            result = None
            for _ in range(n):
                if result is None:
                    result = fn(*args, **kwargs)
                else:
                    result = fn(result)
            return result

        return decorating

    return decorator


@zlozenie(3)
def f1(x):
    return x + 1


@zlozenie(2)
def f2(x):
    return x * x


@zlozenie(5)
def f3(word):
    return "".join(chr(ord(l) + 1) for l in word)


print(f1(2) == 5)
print(f2(3) == 81)
print(f3("alamakota") == "fqfrfptyf")

dictionary = {
    1: (lambda x, y: y * y),
    2: (lambda x, y: x + y),
    3: (lambda x, y: x * y),
    4: (lambda x, y: 0),

}


def my_function(x, y):
    return dictionary[x](x, y)


print(my_function(1, 3) == 9)
print(my_function(2, 4) == 6)
print(my_function(3, 1) == 3)
print(my_function(4, 9) == 0)
