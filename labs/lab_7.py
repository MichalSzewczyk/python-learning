import json
from optparse import OptionParser

parser = OptionParser()
parser.add_option('-p', dest='start_point', help='Start point')
parser.add_option('-s', dest='step', help='Step size')
parser.add_option('-n', dest='number_of_steps', help='Steps number')
parser.add_option('-a', dest='accuracy', help='Accuracy')
options, args = parser.parse_args()
print(args)


class Payload(object):
     def __init__(self, j):
         self.__dict__ = json.loads(j)

with open('timezone.data', 'r') as myfile:
    data=myfile.read().replace('\n', '')

print(data)
payload = Payload(data)

print(payload)