# Przygotuj funkcję, która usunie duplikaty z listy.
import collections

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


