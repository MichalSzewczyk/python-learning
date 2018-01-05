import numpy as np
import pandas as pd

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

# Series have the feature which enables us to replace elements also in two ways -
# by index and by label, but new value has to be of the same type as previous one:
s[0] = 10
s['b'] = 20
s['c'] = None
print(s)

# It's also possible to change value of multiple values which satisfies given condition:
s[s < 5] = 10
print(s)

# We can perform logical operations on series, in that case logical operation is performed for each element in series:
print(s < 10)
# Verify if given key is in the series
print('a' in s)

# We can perform mathematical operations on series:
# Operations between two series
s1 = pd.Series([3, 1, 4, 2, 5, 8, 7, 9, None])
s2 = pd.Series([30, 10, 40, 20, 5, 8, 7, 9])
print(s1 - s2)
print(s1 + s2)
print(s1 * s2)
print(s1 / s2)
# Operations between series and
print(s1 - 7)
print(s1 + 7)
print(s1 * 7)
print(s1 / 7)
# And perform operations from numpy lib
print(np.square(s1))

# Verification if elements are defined:
print(s1.notnull())
print(s1.isnull())

# Get only defined elements:
print(s1[s1.notnull()])

# It's possible to define the name of the series
s.name = 'my_series_name'
print(s)
