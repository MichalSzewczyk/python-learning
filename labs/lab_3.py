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
