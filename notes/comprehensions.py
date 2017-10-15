# Comprehensions - generates sequence from other sequence
# idea: [ funtion(variable) for variable in sequence if predicate(variable) ]
# list comprehension - odd numbers:
list = [x for x in range(7) if x % 2]
print(list)

# set comprehension - odd numbers:
set = {x for x in range(7) if x % 2}
print(set)

# dictionary comprehension - odd numbers with indexes:
dict = {index: x for (index, x) in enumerate(range(7)) if x % 2}
print(dict)