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


