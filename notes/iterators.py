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
result = reduce(lambda x,y: str(x)+str(y), map(lambda x: list(x), itertools.tee(range(20), 5)))
print(result)