import pandas as pd
from pandas import Series

# Pandas - is an open source library created in order to give support for easy data analysis
# Pandas adds two new data structures to python:
# Series - like array or list - ordered, single axis data structure where each element has a label. By default labels of
# each elements are theirs indexes

# Create series of elements of any type
s = pd.Series(['values', 0, 'can', [], 'be', (), 'of', {}, 'any', (()), 'type'])
print(s)

# Create series of elements with custom indexes:
s = pd.Series(['foo', 'bar'], index=['idx1', 10])
print(s)

# Series constructor is overloaded to create series from dictionary:
d = {0: 'k1', 'idx2': 'k2', 2: 'k3', 'test': 'k4', }
s = pd.Series(d)
print(s)

# And combine both methods
# In that case indexes will determine the order of elements in series
s = pd.Series(d, index=[0, 'test', 2])
print(s)

# If the first argument is single value, then this value will be duplicated for each index
s = pd.Series('test', index=['foo', 'bar'])
print(s)

s = pd.Series([7, 3, 2, 1], index=['a', 'b', 'c', 'd', ])
# It is possible to access elements of series by it's index (position in order of declaration)
print(s[0])
# print(s.get_value(0)) - works but deprecated

# Or get all values from series:
print(s.get_values())

# Get value by label
print(s.at['c'])

# Get value by index
print(s.iat[0])

# Get sub series in typical way:
print(s[0:2:1])

# Get sub series of elements which satisfies given condition
print(s[s < 2])

# Get sub series of elements which satisfies given condition
print(s[s < 2])

# We can get value by index or label in the same way:
print(s[0], s['a'])

# Or get value or default value:
print(s.get('not_present', 'default'))

