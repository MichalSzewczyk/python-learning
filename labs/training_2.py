# Przygotuj funkcję, która usunie duplikaty z listy.
import collections

from collections import defaultdict

my_list = ['art', 'lean', 'desk', 'flavor', 'compare', 'secretive', 'narrow', 'flavor', 'flavor', 'miami', 'teaching',
           'fire', 'rate', 'light', 'jump', 'offer', 'fold', 'abstract', 'box', 'story', 'bomb', 'grape', 'grin',
           'jackhammer', 'torchlight', 'flugelhorn', 'verkrampte', 'grandchild', 'witchcraft', 'pawnbroker',
           'cowpuncher', 'grandchild', 'protectrix', 'python', 'java', 'c++', 'monitor', 'mafia', 'think',
           'new', 'york', 'fold', 'abstract', 'box', 'story', 'bomb', 'grape', 'grin', 'jackhammer', 'torchlight',
           'flugelhorn', 'verkrampte', 'grandchild', 'witchcraft', 'pawnbroker', 'cowpuncher', 'grandchild',
           'protectrix', 'python', 'java', 'c++', 'monitor', 'mafia', 'think', 'new', 'york', 'anaconda', 'apple',
           'banana', 'shake', 'ipod', 'mutation', 'process', 'thread', 'water', 'drink', 'tea', 'cola', 'fender',
           'steering', 'wheel', 'grape', 'bean', 'eban', 'iphone', 'android', 'keyboard', 'thinking', 'speaker', 'loud',
           'permission', 'denied', 'natural', 'language', 'miracle', 'my', 'name', 'is', 'bond', 'dance']


def f(given_list):
    return set(given_list)


print(len(f(my_list)) == 71)

#
# Popraw poniższy kod na bardziej optymalny (wykorzystaj collections.Counter)
A = ["Cupcake", "ipsum", "dolor", "sit", "amet", "marshmallow", "Cupcake", "ipsum", "Cupcake"]

print(collections.Counter(A).most_common())

import numpy as np

x = np.array(
    [[-2, 2, 3, 4],
     [5, 3, -1, 8],
     [9, -4, 11, 12]])

print(np.argwhere(x < 3).sum())


def f1(message1, message2):
    return (message1[2] == message2[2]) and (message1[-2] == message2[- 2])


print(f1("abarypxtw", "orakkkasdto"))

import itertools


def bin_num_gen(N):
    """ Funkcja generuje liste stringów, reprezentujących kolejne liczby binarne od 0 do 2^n.
    Bonusowe punkty za one-liner"""
    return ["{0:b}".format(i) for i in range(0, 2 ** N)]


print(bin_num_gen(4))
print(bin_num_gen(4) == ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010',
                         '1011', '1100', '1101', '1110', '1111'])


def make_big_and_ordered(words, order):
    """ Funkcja przyjmuje listę słów oraz listę liczb od 1 do N, gdzie N = długość listy słów.
        Zwraca string złożony ze słów rzutowanych na duże listery, w kolejności zgodnej z order
        Bonus za one-liner"""
    return ' '.join(
        i.upper() for i in map(lambda value: value[0], sorted(zip(words, order), key=lambda value: value[1])))


words = ['kota', 'ala', 'ma']
order = [3, 1, 2]

print(make_big_and_ordered(words, order))
print(make_big_and_ordered(words, order) == "ALA MA KOTA")

# Dlaczego powyższy kod nie działa? Poprawić go.
import copy

a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]

d = copy.deepcopy(c)
c[0][0] = "A"
assert (d[0][0] == 1)

people = [('Smith', ('C++', 'Advanced')),
          ('Mary', ('Java', 'Beginner')),
          ('John', ('Python', 'Intermediate')),
          ('Smith', ('Java', 'Intermediate')),
          ('Agnes', ('Python', 'Beginner')),
          ('Mary', ('C#', 'Advanced'))]

d = defaultdict(lambda: [])

for person, skill in people:
    d[person].append(skill)

print(list(d.items()))


