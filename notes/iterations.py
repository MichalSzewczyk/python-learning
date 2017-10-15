# False in python:
bool(None)
bool(False)
bool([])  # Every empty collection is false
bool(0)
bool(0.0)
bool('')

# Verify if collection is empty:
anyList = []
if list:
    pass  # process if not empty
else:
    print('Empty list!')

# Range
# range 0 - n-1, n = 10
range(10)
# range n1 - n2-1, n1 = 10, n2 = 20
range(10, 20)
# range n1 - n2-1 with step m, n1 = 10, n2 = 20, m=2
range(10, 20, 2)

# zip - generates pairs from passed values:
for i, j in zip('foo'.split(), 'bar'.split()):
    print(i + j)

# iterate with index:
for (index, value) in ['foo', 'bar', 'foobar']:
    print('Element ' + value + 'available on index ' + index)
