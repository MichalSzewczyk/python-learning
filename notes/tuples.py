# Tuple
# tuple - immutable, ordered collection
any_tuple = (0, 'asd', [])
# comma separated values  are converted to a tuple:
t = 'foo', 'bar', 'foobar'

# to iterate over collection with index use enumerate:
for index, value in enumerate(('any', 'basic', 'touple')):
    pass
# tuples are immutable but can contain mutable elements:
any_tuple = (['foo'], [0, 1])
any_tuple[0].append('bar')

# tuple definition
tuple = (1, 2, 3)
print(tuple)

# tuple with one element needs to have comma after element
invalid_single_element_tuple = (1)  # integer declaration
print(type(invalid_single_element_tuple))
valid_single_element_tuple = (1,)
print(type(valid_single_element_tuple))
multi_element_tuple = (1, 2, 3)
empty_tuple = ()

# unpack tuple into variables:
a, b, c = (1, 2, 3)
a, *b, c = (1, 2, 3, 4)
