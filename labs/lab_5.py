# ZAD 1
class FrozenDictionary(object):
    """
    Odpowiednik frozenset dla zbiorów, czyli słownik, który nie jest modyfikowalny,
    a dzięki temu może być np. elementem zbiorów, albo kluczem w innym słowniku.
    """

    def __init__(self, dictionary):
        """Tworzy nowy zamrożony słownik z podanego słownika"""
        self.internal_dict = {}
        for i in dictionary.items():
            self.internal_dict[i[0]] = i[1]

    def __hash__(self):
        """Zwraca hasz słownika (int)"""
        result = 0
        for i in self.internal_dict.items():
            result += hash(i[0]) + hash(i[1])
        return result

    def __eq__(self, d):
        """Porównuje nasz słownik z zamrożonym słownikiem d"""
        for i in self.internal_dict.items():
            if d.internal_dict[i[0]] != i[1]:
                return False
        return True

    def __repr__(self):
        """Zwraca reprezentację naszego słownika jako string"""
        result = ""
        for i in self.internal_dict.items():
            result += '\'' + str(i[0]) + '\'=''\'' + str(i[1]) + '\''
        return result


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


# ZAD 2
class BagOfWords:
    def __init__(self, text):
        if isinstance(text, str):
            self.dictionary = self.get_dict_from_list_of_words(text.split(' '))
        else:
            with text as f:
                self.dictionary = self.get_dict_from_list_of_words(f.read().split(' '))

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


bow = BagOfWords("ala ma kota ala ma ala")
print('ala' in bow)
for word in bow:
    print(word)

bow = BagOfWords(open("plik.txt"))
bow1 = BagOfWords("ala ma kota ala ma ala")
bow2 = BagOfWords("tomek tez ma kota")
bow3 = bow1 + bow2
print('tomek' in bow1)  # False
print('tomek' in bow3)  # True
print('ala' in bow3)  # True
print(bow3)  # ala:3, ma:3, kota:2, tez:1, tomek:1
print(bow1["ala"])  # 3
print(bow3["ala"])  # 3

bow3['tomek'] = 10
for el in bow3:
    print(el)


# ZAD 3
class BagOfPairsOfWords(BagOfWords):
    def __init__(self, text):
        super().__init__(text)

    def __repr__(self):
        result = ''
        for item in self.dictionary.items():
            result += item[0] + ' '
        return result

    def get_dict_from_list_of_words(self, word_list):
        dictionary = {}
        prev = None
        for word in word_list:
            actual = (prev, word)
            if actual not in dictionary.keys():
                dictionary[actual] = 0
            dictionary[actual] += 1
            prev = word

        end = (prev, None)
        if end not in dictionary.keys():
            dictionary[end] = 0
        dictionary[end] += 1
        return dictionary

    def __iter__(self):
        for item in sorted(self.dictionary, key=lambda x: str(x[0])):
            yield item


bopow = BagOfPairsOfWords('ala ma kota ala ma psa')
print(bopow[('ala', 'ma')] == 2)
print(('ala', 'ma') in bopow)
for word1, word2 in bopow:
    print(word1, word2, bopow[(word1, word2)])
