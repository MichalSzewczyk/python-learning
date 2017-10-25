def log(text, *args):
    " Wypisuje wiadomosc opcjonalnie wraz z podaną wartoscią "
    if len(args) == 0:
        print(text)
    if len(args) > 1:
        raise Exception
    else:
        for value in args:
            print(text + ": " + str(value))


log("Hello World!")  # Hello World!
log("The value is", 42)  # The value is: 42


def mean(*args):
    """Zwraca średnią liczb podanych jako argumenty pozycyjne"""
    sum = 0
    for arg in args:
        sum += arg
    return sum / len(args)


print(mean(1, 2, 3) == 2)
print(mean(2, 2, 4, 4) == 3)
print(mean(1, 2, 3, 4, 5, 61, 2, 12, 123, 123) == 33.6)


def check_dictionary_content(dictionary, **kwargs):
    """Sprawdza, czy w danym słowniku znajduje się conajmniej podana liczba elementów"""
    values = {}
    for k, v in kwargs.items():
        if k in values.keys():
            values[k] += v
        else:
            values[k] = v
    for value in values.keys():
        if value not in dictionary.keys() or dictionary[value] < values[value]:
            return False
    return True


# print(check_dictionary_content({}, orange=2))

d = {'orange': 3, 'apple': 1, 'dogs': 10}
print(check_dictionary_content(d, orange=2) == True)
print(check_dictionary_content(d, orange=2, apple=1) == True)
print(check_dictionary_content(d, dogs=11) == False)
print(check_dictionary_content(d, dogs=9, cats=0) == True)
print(check_dictionary_content(d, apple=0, cats=1) == False)
print(check_dictionary_content(d, **d) == True)


def natural_numbers(k=0):
    """Tworzy generator liczb naturalnych od liczby k"""
    while (True):
        k += 1
        yield k - 1


import types

print(isinstance(natural_numbers(), types.GeneratorType))

for i, n in enumerate(natural_numbers()):
    print(i, i == n)
    if i > 20:
        break

for i, n in enumerate(natural_numbers(1)):
    print(i, i + 1 == n)
    if i > 20:
        break


def factorials():
    actual = 1
    yield actual
    counter = 1
    while (True):
        yield actual
        counter += 1
        actual *= (counter)


import types

print(isinstance(factorials(), types.GeneratorType))

results = [1, 1, 2, 6, 24, 120, 720, 5040]
for truth, answer in zip(results, factorials()):
    print(truth, truth == answer)

from random import random


class cached(object):
    def __init__(self, func):
        self.func = func
        self.called_counter = 0
        self.evaluated_counter = 0
        self.invocation_map = {}

    def __call__(self, *args, **kwargs):
        converted = wrap(args, kwargs)
        self.called_counter += 1
        if (converted) in self.invocation_map.keys():
            return self.invocation_map[converted]
        else:
            self.evaluated_counter += 1
            self.invocation_map[converted] = self.func(args, kwargs)
            return self.invocation_map[wrap(args, kwargs)]

    def cache_reset(self):
        self.invocation_map.clear()

    def cache_status(self):
        return 'Function foo called ' + str(self.called_counter) + ' times, evaluated ' + str(
            self.evaluated_counter) + ' times'


def wrap(args, kwargs):
    key = str(sorted(args)) + str(sorted([str(k) for k in kwargs]))
    return key


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


def f(n):
    for i in range(2, n - 1):
        if not n % i:
            return False
    return True


print(f(8))
