import re

pattern = 'RUN \d{6} COMPLETED. OUTPUT IN FILE \w+.dat. .*'
# ex2
with open('atoms.log') as atoms:
    for line in atoms:
        if re.search(pattern, line) is not None:
            print(line)

# ex3
# Jun 29 20:18:40 noether sshd[5805]: Invalid user tester from 218.189.194.200
# Niepoprawna nazwa użytkownika: "tester", połaczenie z 218.189.194.200 nawiązano 29 czerwca o godz. 20:18
pattern = '(\w{3} \d{2} \d{2}:\d{2}:\d{2}) noether sshd\[5805\]: Invalid user (\w+) from (\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})'
result = 'Niepoprawna nazwa użytkownika: "{}", połaczenie z {} nawiązano {}'


def convert_to_pl_month(month):
    month = month.lower()
    if month == 'jan':
        return 'stycznia'
    elif month == 'feb':
        return 'lutego'
    elif month == 'mar':
        return 'marca'
    elif month == 'apr':
        return 'kwietnia'
    elif month == 'may':
        return 'maja'
    elif month == 'jun':
        return 'czerwca'
    elif month == 'jul':
        return 'lipca'
    elif month == 'oug':
        return 'sierpnia'
    elif month == 'sep':
        return 'wrzesnia'
    elif month == 'oct':
        return 'pazdziernika'
    elif month == 'now':
        return 'listopada'
    elif month == 'dec':
        return 'grudnia'
    else:
        print('fail')


def convert_date(date_string: str):
    result = ''
    result += date_string[4:6] + ' '
    result += convert_to_pl_month(date_string[0:3]) + ' o godzinie '
    result += date_string[7:12]
    return result


print(convert_date('Jun 29 20:18:40'))

with open('messages.txt') as messages:
    for line in messages:
        search_result = re.search(pattern, line)
        if search_result is not None:
            print(result.format(search_result.group(2), search_result.group(3), convert_date(search_result.group(1))))

# ex4

from collections import defaultdict


def count_letters(word):
    """ Zwraca slownik gdzie kluczami sa litery, a wartosci ilosc ich wystepowania """
    result_dict = defaultdict(lambda: 0)
    for i in word:
        result_dict[i] += 1
    return result_dict


print(count_letters('aaaaa') == {'a': 5})
print(count_letters('abbccaaaa') == {'a': 5, 'b': 2, 'c': 2})
print(count_letters('abc') == {'a': 1, 'b': 1, 'c': 1})


def group_words_by_first_letter(text):
    """ Dzieli tekst po spacjach i zwraca slownik gdzie kluczami sa pierwsze litery, a wartosciami listy slow zaczynajacych sie na te litery"""
    result_dict = defaultdict(lambda: [])
    for i in text.split(' '):
        result_dict[i[0]].append(i)
    return result_dict


print(group_words_by_first_letter("ala ma kota") == {'a': ['ala'], 'm': ['ma'], 'k': ['kota']})
print(group_words_by_first_letter("ala ma kota ala ma psa") == {'a': ['ala', 'ala'], 'm': ['ma', 'ma'], 'k': ['kota'],
                                                                'p': ['psa']})
print(group_words_by_first_letter("ala ma kota ale marysia ma konia") == {'a': ['ala', 'ale'],
                                                                          'm': ['ma', 'marysia', 'ma'],
                                                                          'k': ['kota', 'konia']})


class FrozenDictionary(object):
    """
    Odpowiednik frozenset dla zbiorów, czyli słownik, który nie jest modyfikowalny,
    a dzięki temu może być np. elementem zbiorów, albo kluczem w innym słowniku.
    """

    def __init__(self, dictionary):
        """Tworzy nowy zamrożony słownik z podanego słownika"""
        self.f_dict = dictionary

    def __hash__(self):
        """Zwraca hasz słownika (int)"""
        result = 0
        for i in self.f_dict:
            result += hash(i)
        return result

    def __eq__(self, d: dict):
        """Porównuje nasz słownik z zamrożonym słownikiem d"""
        return self.f_dict == d.f_dict

    def __repr__(self):
        """Zwraca reprezentację naszego słownika jako string"""
        return str(self.f_dict)


dicts = [FrozenDictionary({'ala': 4}),
         FrozenDictionary({'ala': 1, 'jacek': 0}),
         FrozenDictionary({'ala': 4}),
         FrozenDictionary({'ala': 2}),
         FrozenDictionary({'jacek': 0, 'ala': 1})]

s = set(dicts)
print(dicts[0] == dicts[2])
print(dicts[0] != dicts[3])
print(len(s) == 3)
for d in dicts:
    print(d in s)

# Powinno wyświetlić coś w stylu set([{'ala': 4}, {'ala': 1, 'jacek': 0}, {'ala': 2}])
print(s)
d1 = {'b': 2, 'a': 1, }
d2 = {'a': 1, 'b': 2}
print(d1 == d2)


# ex5

class BagOfWords:
    def __init__(self, text):
        self.result = defaultdict(lambda: 0)
        for word in text.split(' '):
            self.result[word] += 1

    def __str__(self):
        return str(self.result)

    def __contains__(self, item):
        return item in self.result.keys()

    def __iter__(self):
        return map(lambda item: item[0], sorted(self.result.items(), key=lambda item1: -item1[1]))

    def __add__(self, other):
        return dict(list(self.result.items()) + list(other.result.items()))

    def __getitem__(self, item):
        return self.result[item]

bow = BagOfWords('asd dsa rfe3wr ads asd asd asd dsa qwe4 4wq 4wq 4wq 4wq 4wq')
bow2 = BagOfWords('asd!! dsa rfe3wr ads asd asd asd dsa qwe4 4wq 4wq 4wq 4wq 4wq')
print(bow)
for i in bow:
    print(i)

print(bow + bow2)
print(bow['asd'])
