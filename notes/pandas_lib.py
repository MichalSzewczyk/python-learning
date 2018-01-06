import numpy as np
import pandas as pd
import pylab

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

# DataFrame - data structure, which consists of rows and cols, similar to excel table
# Create DataFrame from dictionary:
df = pd.DataFrame({'col_1': ['row_1_in_col_1', 'row_2_in_col_1', 'row_3_in_col_1', ],
                   'col_2': ['row_1_in_col_2', 'row_2_in_col_2', 'row_3_in_col_2', ],
                   'col_3': ['row_1_in_col_3', 'row_2_in_col_3', 'row_3_in_col_3', ]},
                  index=['row_1', 'row_2', 'row_3', ])
print(df)

# Create DataFrame from Series:
df = pd.DataFrame({'col_1': pd.Series(['row_1_in_col_1', 'row_2_in_col_1', ], index=['row_1', 'row_2']),
                   'col_2': pd.Series(['row_1_in_col_2', 'row_2_in_col_2', ], index=['row_1', 'row_3'])}, )
print(df)

# Specify which columns and rows should be shown - if values for given column/row are not present,
# then there are NaN/None values inserted:
df = pd.DataFrame({'col_1': pd.Series({1: 'row_1_col_1', 2: 'row_2_col_1'}),
                   'col_2': pd.Series({1: 'row_1_col_2', 3: 'row_2_col_2'})}, columns=['col_1', 'col_2'],
                  index=[1, 2, 3, 4])

print(df)

# Ways to get information about data inside DataFrame:
# Get basic information such as: size, type of rows/cols, amount of RAM usage to store this DataFrame instance
print(df.info())
# Get information about types of columns
print(df.dtypes)
# Get name of index under given index:
print(df.index[0])
# Get all indexes:
print(df.index)
# Get name of column under given index:
print(df.columns[0])
# Get all columns:
print(df.columns)
# Get all of the basic statistics about given DataFrame:
print(df.describe())
# Get specified basic statistics about given DataFrame:
print(df.describe().loc[['count', 'unique']])

# We can easily get records from DataFrame in many ways:
# Get first records:
print(df.head(2))

# Or get first records for only one column:
print(df['col_1'].head(2))

# Get the last elements:
print(df.tail(2))

# We can also modify DataFrame:
# We can modify DataFrame by specified column (not by index as it is by default)
print(df.set_index('col_1'))

# By default set_index returns new DataFrame, but it is possible to modify current DataFrame:
print(df.set_index('col_1', inplace=True))

# Ways of data retrieval
data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
        'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions', 'Lions', 'Lions'],
        'wins': [11, 8, 10, 15, 11, 6, 10, 4],
        'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
football = pd.DataFrame(data)
print(football)

# Get single column:
print(football['year'])

# Get more then one column:
print(football[['year', 'team']])

# Get specified rows by index:
print(football.loc[2:3])

# Get specified rows by their position:
print(football.iloc[2:3])

# Get sub DataFrame from current DataFrame:
print(football.loc[2:3, ['team', 'wins']])

# Get single element by labels:
print(football.at[0, 'team'])

# Or by position:
print(football.iat[0, 1])

# Get only those values, which satisfies given predicate:
print(football[football.year > 2011])

# Get only those values, which satisfies given predicate:
print(football[football.year > 2011])

# Get maximum value from given column:
print(football['year'].max())

# Get mean value from given column:
print(football['year'].mean())

# Get mean values for given columns:
print(football[['year', 'losses']].mean())

# Modify existing values of given cells:
football.loc[2, ['losses']] = 'test'
print(football)

# Or modify all rows in single column:
football['losses'] = 0
print(football)

# Transpose matrix:
print(football.T)

# Increment values in single col:
print(football['losses'] + 10)

# Delete the whole column:
del football['losses']
print(football)

# Delete the whole row:
print(football[football.index != 0])

# Sorting:
# Sort rows by index - descending:
print(football.sort_index(axis=0, ascending=False))

# Sort cols by index - descending:
print(football.sort_index(axis=1, ascending=True))

# Sort rows by specified column:
print(football.sort_values('wins'))

# Join DataFrames:
left_frame = pd.DataFrame({'key': range(5),
                           'left_value': ['a', 'b', 'c', 'd', 'e']})
right_frame = pd.DataFrame({'key': range(2, 7),
                            'right_value': ['f', 'g', 'h', 'i', 'j']})

print(left_frame)
print(right_frame)

# Define col on which merging is performed and merging policy: how can be on of: left/right/inner/outer
print(pd.merge(left_frame, right_frame, on='key', how='outer'))

# Concatenate two DataFrames on given axis:

# Add next rows
print(pd.concat([left_frame, right_frame], axis=0))

# Add next cols
print(pd.concat([left_frame, right_frame], axis=1))

# Flatten all columns
print(football.unstack())

# Flatten all columns
print(football.stack())

# Import/export

# Export to csv
# football.to_csv('file_name')
# Import from csv
# df = pd.read_csv('file_name')

# Export to excel file, installation required: !pip install xlwt
# football.to_excel('file_name', sheet_name='some sheet')

# Import from excel file:
# pd.read_excel('dane.xls')

# Export to txt:
# football.to_csv('file.txt')

# Import from txt
# pd.read_csv('file.txt')

# football.cumsum()
# football.plot(figsize=(10, 10))

# pylab.show()
