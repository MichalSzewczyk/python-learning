# Przygotuj funkcję, która usunie duplikaty z listy.
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

d = dict()
for a in A:
    if a not in d:
        d[a] = 1
    else:
        d[a] += 1

most_common = []
for key in sorted(d, key=d.get, reverse=True)[:3]:
    most_common.append((key, d[key]))
    print("%s: %i" % (key, d[key]))

print(most_common)