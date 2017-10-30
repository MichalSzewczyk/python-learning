# map(fn, inter) - applies function to each argument returned from iterable:
from functools import reduce

iter = ['foo', 'bar', 'foobar']
fn = lambda x: len(x)
result = map(fn, iter)

print(list(result))

# filter(pred, iter) - filters elements from iterable, returns only those, for which predicate returned true
iter = ['foo', 'bar', 'foobar']
pred = lambda x: len(x) == 3
result = filter(pred, iter)

print(list(result))

# reduce(func, iter) - reduces values from iter to single value using func to merge actual result with next element:
iter = ['foo', 'bar', 'foobar']
func = lambda x, y: x + y
result = reduce(func, iter)

print(result)


# list comprehensions - huge disadvantage of this approach is that each element
# is processed even if it is unnecessary - eager creation:
def convert_to_char(i):
    result = chr(i)
    print('Converted {}.'.format(result))
    return result


print([convert_to_char(x) for x in range(ord('a'), ord('z') + 1)])
if 'e' in [convert_to_char(x) for x in range(ord('a'), ord('z') + 1)]:
    print('e in collection!\n')

# generator expressions - generates values only if necessary - lazy creation:

if 'e' in (convert_to_char(x) for x in range(ord('a'), ord('z') + 1)):
    print('e in collection!\n')

# verify if all elements in collection are true:
if not all([False, True, True, False]):
    print('Not all elements are true.')

# verify if any of elements in list is true:
if any([False, True, True, False]):
    print('There is element which is True')
