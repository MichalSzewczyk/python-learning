def _filter(func=None, iterable=[]):
    """Filtruje z iterable elementy, dla których funkcja func zwraca False zostawiając pozostałe"""
    for value in iterable:
        if func(value):
            pass



from types import GeneratorType

print(isinstance(_filter(), GeneratorType))
print(list(filter(lambda x: x > 0, [0, -3, 1, 6])) == list(_filter(lambda x: x > 0, [0, -3, 1, 6])))
print(list(filter(None, [2, -3, 1, 6])) == list(_filter(None, [2, -3, 1, 6])))
print(list(filter(None, [True, False, False])) == list(_filter(None, [True, False, False])))
print(list(filter(None, [0, -3, 1, 6])) == list(_filter(None, [0, -3, 1, 6])))