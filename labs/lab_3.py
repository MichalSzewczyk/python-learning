from functools import reduce
from itertools import chain

import collections
from random import random, randint


def log(text, optional=None):
    " Wypisuje wiadomosc opcjonalnie wraz z podaną wartoscią "
    if optional is None:
        print(text)
    else:
        print(text + ': {}'.format(optional))


log("Hello World!")  # Hello World!
log("The value is", 42)  # The value is: 42


def mean(*args):
    """Zwraca średnią liczb podanych jako argumenty pozycyjne"""
    return reduce(lambda x, y: x + y, args) / len(args)


print(mean(1, 2, 3) == 2)
print(mean(2, 2, 4, 4) == 3)
print(mean(1, 2, 3, 4, 5, 61, 2, 12, 123, 123) == 33.6)


def check_dictionary_content(dictionary, **kwargs):
    """Sprawdza, czy w danym słowniku znajduje się conajmniej podana liczba elementów"""
    return all(map(
        lambda x: (dictionary.get(x[0]) is not None) and dictionary[x[0]] >= x[1] or dictionary.get(x[0]) is None and x[
                                                                                                                          1] == 0,
        kwargs.items()))


d = {'orange': 3, 'apple': 1, 'dogs': 10}
print(check_dictionary_content(d, orange=2) == True)
print(check_dictionary_content(d, orange=2, apple=1) == True)
print(check_dictionary_content(d, dogs=11) == False)
print(check_dictionary_content(d, dogs=9, cats=0) == True)
print(check_dictionary_content(d, apple=0, cats=1) == False)
print(check_dictionary_content(d, **d) == True)


def show_my_args(*args):  # a
    if len(args) == 0:
        return ''
    return reduce(lambda x, y: x + '\n' + y, map(lambda x: '{}:{}'.format(type(x).__name__, x), args))


print(show_my_args() == "")
print(show_my_args(1, "1", 1.1) == "int:1\nstr:1\nfloat:1.1")
print(show_my_args([1, 2], {1: 1, 2: 2}, {1, 2}) == "list:[1, 2]\ndict:{1: 1, 2: 2}\nset:set([1, 2])")


def show_my_kwargs(**kwargs):  # a
    if len(kwargs) == 0:
        return ''
    return reduce(lambda x, y: x + '\n' + y, map(lambda x: '{}:{}'.format(x[0], x[1]), kwargs.items()))


print(show_my_kwargs() == "")
print(show_my_kwargs(a=1, b="1", c=1.1) == "a:1\nc:1.1\nb:1")  # moze nie wyjsc z powodu innej kolejnosci


# print(show_my_kwargs(1))  # TypeError


def show_my_args_kwargs(*args, **kwargs):
    return reduce(lambda x, y: x + '\n' + y, chain(map(lambda x: '{}={}'.format(type(x).__name__, x), args),
                                                   map(lambda x: '{}={}'.format(x[0], x[1]), kwargs.items())))


print(show_my_args_kwargs(1, b="1", c=1.1))


def numbers_to_percents(values):
    values_sum = sum(values)
    return list(map(lambda v: v / values_sum if not isinstance(v, collections.Iterable) else 0, values))


print(numbers_to_percents([1, 2, 1]) == [0.25, 0.5, 0.25])
print(numbers_to_percents([1]) == [1])
print(numbers_to_percents([1, 2, 3, 4]) == [0.1, 0.2, 0.3, 0.4])
print(numbers_to_percents(i for i in range(5)))


def zwroc_rosnace(fn, *args):
    return list(filter(lambda arg: fn(arg) > arg, args))


def f1(n):
    return n ** 2 - 3 * n


def f2(n):
    return 100 - n


def f3(word):
    return word[::-1]


print(zwroc_rosnace(f1, 4, 6, 2, -5) == [6, -5])
print(zwroc_rosnace(f2, *range(100)) == list(range(50)))
print(zwroc_rosnace(f3, "python", "nie", "jest", "bardzo", "fajny") == ['jest', 'bardzo', 'fajny'])


def zwroc_rosnace_wzgledem_popredniego(fn, *args):
    prev = None
    result = []
    for i in args:
        actual = fn(i)
        if prev is not None and actual > prev:
            result.append(i)
        prev = actual
    return result


def f1(n):
    return n ** 2 - 3 * n


def f2(n):
    return 100 - n


def f3(word):
    return word[::-1]


print(zwroc_rosnace_wzgledem_popredniego(f1, 4, -5, 6, 2) == [-5])
print(zwroc_rosnace_wzgledem_popredniego(f2, *range(100)) == [])


class Outer:
    counter = 0


def ile_wywolana():
    Outer.counter += 1

    return Outer.counter


print(zwroc_rosnace_wzgledem_popredniego(f3, "python", "nie", "jest", "bardzo", "fajny") == ['jest', 'fajny'])

print(ile_wywolana() == 1)
print(ile_wywolana() == 2)
print(ile_wywolana() == 3)


def get_primes(number):
    primes = []
    counter = 2
    while True:
        is_prime = True
        for i in primes:
            if counter % i is 0:
                is_prime = False
                break
        if is_prime:
            primes.append(counter)
            if counter >= number:
                yield counter
        counter += 1


# for i in get_primes(10):
#     print(i)
# print(get_primes(10))


def lotto():
    counter = 0
    while counter < 6:
        counter += 1
        yield randint(1, 49)


for i in lotto():
    print(i)


