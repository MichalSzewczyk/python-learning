# List - finite, ordered, mutable sequence of data
# can contain elements of single type:
[1, 2, 3, 4]
# or mix of types:
[1, 'foo', True, ()]

# Add element at the end of a list:
l = []
l.append('foo')

# access element on specified index:
l = ['foo', 'bar']
l[0]  # returns foo

# slice list:
l[2:7:2]

# list can contain anything, ie other lists:
[['foo'], ['bar']]

list = ['foo', 'bar']
# List can be extended in three ways:
# pass iterable to extend method:
iterable = range(7)
list.extend(iterable)
# insert element at specified index:
list.insert(0, 'foobar')
# append element at the end
list.append('foobar')
# remove elements from list:
list.remove('bar')
# remove all elements from list:
list.clear()
list = ['foo', 'bar']
# count all occurrences of value in list:
list.count('foo')
# get index of first occurrence in given range
list.index('foo', 0, 7)
# remove and return last element from list:
list.pop()
# remove and return element from list at specified index
list.pop(0)
# stable sort:
list.sort()
# reverse list:
list.reverse()
# get list length:
len(list)
# verify presence of element in list:
'foo' in list

# list declaration:
li = ['foo', 'bar']

# verify if list contains element:
print('foo' in li)

# get list length
len(li)

# add element at the end of a list
li.append('foobar')

# get last element from the list
li.pop()

# access list elements
# first element
li[0]
# last element:
li[-1]

# create a sublist:
li[1:3]
print(li)

# remove element from specified index
del li[0]
print(li)

# remove first occurrence of a value:
li.remove('bar')
print(li)

# insert element at the specific position:
li = ['foo', 'bar']
li.insert(1, "foobar")
print(li)

# list concatenation:
# by addition:
li1 = [1, 2, 3]
li2 = [4, 5, 6, 7]
print(li1 + li2)
# by extend method:
li1.extend(li2)
print(li1)

# access list elements by negative index:
list = [1, 2, 3, 4]
print(list[-1])
# elements can be accessed by index in range: <-n;n)
print(list[-len(list)] == 1)
print(list[len(list) - 1] == 4)
print(list[0] == 1)
print(list[-1] == 4)
# but in negative and positive indexing we can receive index out of bounds exception:
# print(list[-5] == list[4])

# it is possible to create nested lists:
nested_list = [[], [], [], []]
# to access it's elements we have to use [][]
nested_list[1].append(1)
print(nested_list)

# Methods:
any_list = [1, 3, 2, 4]
any_list.extend(range(3))
any_list.clear()
any_list.insert(0, 'test')
any_list.remove('test')
any_list.count('test')
any_list.pop()
any_list.sort()
any_list.reverse()
del any_list[0]

