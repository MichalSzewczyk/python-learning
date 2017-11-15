# Dictionaries
# dictionary - mutable map from hashable values to objects
# object of any type can be the key as long as it's hashable
# empty dictionary definition:
any_dict = {}
# first way of dictionary creation:
any_dict = {'foo': 0, 'bar': 1}
# get value from dict by key:
any_dict['foo']
# modify exiting value:
any_dict['bar'] = 2
# add new value:
any_dict['new'] = 3
# to avoid error when key not exists use 'get' method:
any_dict.get('foo')
# in case of lack of key, it will return 'None'
any_dict.get('not existing key')
# delete element from dict - throw error when key not exists:
del any_dict['foo']
# delete element from dict and return - return default value when not exists:
any_dict.pop('foo', 0)
# delete element from dict and return (removes and return the whole entry - key and value)
any_dict.popitem()
# get all keys from dictionary:
any_dict.keys()
# get all values from dictionary:
any_dict.values()
# get all entries from dictionary (key - value pairs):
any_dict.items()
# verify if entry exists in dictionary:
('foo', 0) in any_dict
# verify number of entries in dictionary:
len(any_dict)
# verify if key is in dictionary:
'key' in any_dict
# copy the dictionary:
any_dict.copy()
# clear the dictionary:
any_dict.clear()

# Dictionary declaration
# empty dict:
any_dict = {}
# fullfiled dict:
any_dict = {"foo": 0, "bar": 1}
# dict = {[]: 0} - raises: TypeError: unhashable type: 'list'
# but tuple as key is ok
any_dict = {(1,): 2}

# get all keys from dictionary:
any_dict.keys()
# get all values from dictionary
any_dict.values()
# check for existence of key:
'key' in any_dict

# get value by key - causes KeyError when not present:
any_dict.setdefault("key", "value")
any_dict['key']

# get value by key - returns none when not present
any_dict.get('key')

# add to key when not present:
any_dict.setdefault('key', 'value')

# override key or add if not present:
any_dict.update({'key2': 'value2'})
print(any_dict)

# delete key-value:
del any_dict['key2']
print(any_dict)

# two ways of dictionary creation:
dictionary_1 = {'foo': 'bar'}
dictionary_2 = dict(foo='bar')
print(dictionary_1 == dictionary_2)

# remove and return value by key:
print(dictionary_1.pop('foo'))
# remove and return the whole entry (the last one)
print(dictionary_2.popitem())

# the following methods are dynamic:
any_dictionary = {1: 2, 3: 4}
keys = any_dictionary.keys()
values = any_dictionary.values()
entries = any_dictionary.items()
any_dictionary.update({5: 6})
print(keys)
print(values)
print(entries)
