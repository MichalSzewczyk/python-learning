from collections import defaultdict


class DictWithDefaultZero(defaultdict):
    def __missing__(self, key):
        value = 0
        self[key] = value
        return value


def count_letters(word):
    """ Zwraca slownik gdzie kluczami sa litery, a wartosci ilosc ich wystepowania """
    my_dict = DictWithDefaultZero()
    for i in word:
        my_dict[i] += 1
    return my_dict


print(count_letters('aaaaa') == {'a': 5})
print(count_letters('abbccaaaa') == {'a': 5, 'b': 2, 'c': 2})
print(count_letters('abc') == {'a': 1, 'b': 1, 'c': 1})


class DictWithDefaultEmptyList(defaultdict):
    def __missing__(self, key):
        value = []
        self[key] = value
        return value


def group_words_by_first_letter(text):
    """ Dzieli tekst po spacjach i zwraca slownik gdzie kluczami sa pierwsze litery, a wartosciami listy slow zaczynajacych sie na te litery"""
    my_dict = DictWithDefaultEmptyList()
    for i in text.split(' '):
        my_dict[i[0]].append(i)
    return my_dict


print(group_words_by_first_letter("ala ma kota") == {'a': ['ala'], 'm': ['ma'], 'k': ['kota']})
print(group_words_by_first_letter("ala ma kota ala ma psa") == {'a': ['ala', 'ala'], 'm': ['ma', 'ma'], 'k': ['kota'],
                                                                'p': ['psa']})
print(group_words_by_first_letter("ala ma kota ale marysia ma konia") == {'a': ['ala', 'ale'],
                                                                          'm': ['ma', 'marysia', 'ma'],
                                                                          'k': ['kota', 'konia']})

# RUN [[NUMER Z DOKŁADNIE 6 CYFR]] COMPLETED. OUTPUT IN FILE [[NAZWA]].dat. [[COKOLWIEK]]
import re

pattern = 'RUN [\d]{6} COMPLETED\. OUTPUT IN FILE .*\.dat\. .*'

with open('atoms.log') as atoms:
    for line in atoms:
        m = re.search(pattern, line)
        if m:
            print(m.group())


# # GIVEN:
# # Jun 29 20:18:40 noether sshd[5805]: Invalid user tester from 218.189.194.200
# # EXPECTED:
# # Niepoprawna nazwa użytkownika: "tester", połaczenie z 218.189.194.200 nawiązano 29 czerwca o godz. 20:18
# pattern = ''
#
# with open('messages.txt') as messages:
#     for line in messages:
#         if ...:
#             print(line)



def prepare(text):
    return re.sub(r'[^A-Za-z\s]+', '', text)


class BagOfWords:
    def __init__(self, text):
        if isinstance(text, str):
            prepared_text = prepare(text)
            self.dictionary = self.get_dict_from_list_of_words(prepared_text.split(' '))
        else:
            with text as f:
                prepared_text = prepare(f.read())
                self.dictionary = self.get_dict_from_list_of_words(prepared_text.split(' '))

    def get_dict_from_list_of_words(self, word_list):
        dictionary = {}
        for word in word_list:
            if word not in dictionary.keys():
                dictionary[word] = 0
            dictionary[word] += 1
        return dictionary

    def __repr__(self):
        result = ''
        for item in self.dictionary.items():
            result += item[0] + ':' + str(item[1]) + ' '
        return result

    def __contains__(self, item):
        return item in self.dictionary

    def __iter__(self):
        for item in sorted(self.dictionary):
            yield item

    def __add__(self, other):
        for i in other.dictionary.items():
            if i[0] in self.dictionary.keys():
                self.dictionary[i[0]] += i[1]
            else:
                self.dictionary[i[0]] = i[1]
        return self

    def __setitem__(self, key, value):
        self.dictionary[key] = value

    def __getitem__(self, item):
        return self.dictionary[item]

bow = BagOfWords(open("data.txt"))
print(bow)