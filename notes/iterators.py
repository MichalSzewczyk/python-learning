# iterator - object which represents finite or infinite data streams.
# Example iterator:
import functools

iterator = iter([1, 2, 3])

# get next element from iterator:
# if iterator is empty rises StopIteration error
next(iterator)

# use iter(structure) to build iterator from data structure
iter([1, 2, 3])

# iterator sees changes to the underlying data structure:
list = [x for x in range(10)]
list_iterator = iter(list)
list.remove(5)
result = functools.reduce(lambda x, y: str(x) + str(y), list_iterator)
print('result: ' + result)

# methods which takes iterator as argument
# consumes iterable until the result is unknown:
list = [1, 2, 3]

# maximum element of the iterable:
max(list)

# minimum element of the iterable:
min(list)

# verification if value is in iterable:
print('foo' in list)

# verification if value isn't in iterable:
print('foo' not in list)

# returns true if all elements in iterable are true:
all(list)

# return true if any of elements in iterable is true:
any(list)

# Methods that returns an iterator:

# returns tuples: (i, value) where i is an index and value i'th value from iterator
for i, j in enumerate([1, 2, 3, 4, ]):
    print('{} on index {}'.format(i, j))

# returns tuples (iter_1[i], iter_2[i], .., iter_n[i]). The number of elements in this
# iterator is equal to number of elements in shortest of the iterators:
for i in zip([1, 2, 3, 4], [1, 2, 3], [5, 6, 7]):
    print(i)

# Tools to play with iterators
import itertools
from functools import reduce

# chain function treats iterators passed as arguments
# as single iterator, by chaining those iterators
# when the first iterator is over then moves to the next

result = reduce(lambda x, y: str(x) + str(y), itertools.chain([1, 2, 3], [4, 5, 6], [7, 8, 9, ]))
print(result)

# cycle function returns iterator that stores all values of iterator inside memory
# and in case of lack of new elements in iterator it will return
# elements of this iterator again

finish = False
result = ''
for i in itertools.cycle(range(10)):
    if i == 9:
        if finish:
            break
        finish = True
    result += str(i)
print(result)

# count returns iterator that consists of consecutive ints starting from n
result = ''
for i in itertools.count(10):
    if i == 20:
        break
    result += str(i)
print(result)

# dropwhile creates an iterator that removes next elements from iterator until
# predicate is satisfied:
result = reduce(lambda x, y: str(x) + str(y), itertools.dropwhile(lambda x: x < 5, range(20)))
print(result)

# islice creates an iterator that slices iterator as [::] expression in lists
# but unlike regular slicing doesn't support legative indexes:
# it takes args:
# iterator - which is the source of elements
# start - index of first element in iterator (None means 0)
# stop - index of last element in iterator (None means last)
# step - (None means 0 step)
result = reduce(lambda x, y: str(x) + str(y), itertools.islice(range(20), 5, 15, 2))
print(result)

# combinations creates iterator with n length subsequences in lexicographic order.
result = reduce(lambda x, y: str(x) + str(y), itertools.combinations(range(10), 4))
print(result)

# tee returns n iterators from single iterator:
# result = reduce(lambda x, y: str(x) + str(y), map(lambda x: list(x), itertools.tee(range(20), 5)))
# print(result)


# range method: range(start_open=0, end_closed, step=1)
# if start is grater then stop and step is incremental then no execution is performed
for i in range(19, 4, 2):
    print(i)
# It is possible to iterate backwards
for i in range(19, 4, -2):
    print(i)
# It is possible to iterate forwards
for i in range(11, 15, 2):
    print(i)
# It is possible to iterate backwards over negative values
for i in range(-4, -19, -2):
    print(i)
# It is possible to iterate forwards over negative values
for i in range(-20, -15, 2):
    print(i)
# By default start is 0 and step is 1:
for i in range(5):
    print(i)

# iterate in reverse order:
for i in reversed(range(10)):
    print(i)