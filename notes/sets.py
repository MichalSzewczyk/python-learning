# Set
# set - unordered collection of distinct, hashable elements
any_set = {0, 1, 2}
# to create empty set we need to use set() instead {}. {} creates empty dictionary:
any_set = set()
# add to set:
any_set.add('3')
# remove value from set:
any_set.remove('3')
# same as remove, but not rise an error when value not exists
any_set.discard(3)
# get last element:
any_set.add(0)
any_set.pop()
# remove all elements
any_set.clear()
# operations on two sets:
first_set = {'f', 'o'}
second_set = {'b', 'a', 'r'}
# set difference:
first_set - second_set
# set union:
first_set | second_set
# set intersection:
first_set & second_set
# symmetric difference:
first_set ^ second_set
