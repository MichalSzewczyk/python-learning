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


