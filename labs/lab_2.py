def check_anagram(first, second):
    """ Sprawdza czy podane słowa są anagramami """
    d = {}

    for character in first:
        if character in d:
            d[character] += 1
        else:
            d[character] = 1

    for character in second:
        if character not in d:
            return False
        elif d[character] is 0:
            return False
        else:
            d[character] -= 1


print(check_anagram("abcd", "dcba") == True)
print(check_anagram("aba", "baa") == True)
print(check_anagram("aba", "ba") == False)
print(check_anagram("tom marvolo riddle ", "i am lord voldemort") == True)

from string import ascii_lowercase


def cipher(word, key):
    """ Funkcja szyfruje słowo `word` używając szyfru podstawieniowego z kluczem `key`. Prosze zalożyć, że słowo
        składa się tylko z małych liter angielskich i spacji"""
    char_tab = list(key)
    result = ""
    for character in word:
        if character == ' ':
            result += ' '
        else:
            result += char_tab[ord(character.lower()) - ord('a')]

    return result


key = "zyxwvutsrqponmlkjihgfedcba"
print(cipher("ala ma kota", key) == "zoz nz plgz")
print(cipher("uniwersytet jagiellonski", key) == "fmrdvihbgvg qztrvoolmhpr")


def even_numbers_from_list(data):
    """Zwraca podlistę "data" zawierającą wyłącznie parzyste liczby"""
    return [x for x in data if x % 2 == 0]


print(even_numbers_from_list([1, 2, 3, 4]) == [2, 4])
print(even_numbers_from_list(range(10)) == list(range(0, 10, 2)))
print(even_numbers_from_list(range(1000)) == list(range(0, 1000, 2)))
print(even_numbers_from_list([10, 2, 3, 4, 6, -3, -4]) == [10, 2, 4, 6, -4])


def words_analyze(words):
    """Zwraca listę trójek, gdzie i'ta trójka to (i, i'te słowo, długość i'tego słowa)"""
    return [(ind, x, len(x)) for ind, x in enumerate(words)]


print(words_analyze(['tomek', 'jadzia']) == [(0, 'tomek', 5), (1, 'jadzia', 6)])
print(words_analyze([]) == [])


def count_words_starting_with_letter(text, letter):
    """Zwraca słownik gdzie kluczami są wszystkie słowa występujące w tekście
    rozpoczynające się na zadaną literę, a wartością ile razy wystąpiy"""
    return {value: text.split(' ').count(value) for value in text.split(' ') if value[0] == letter}


print(count_words_starting_with_letter('ola ma kota o imieniu ola', 'o') == {'ola': 2, 'o': 1})
print(count_words_starting_with_letter('ola ma kota o imieniu ola', 'k') == {'kota': 1})
print(count_words_starting_with_letter('ola ma kota o imieniu ola', 'x') == {})


def dna_to_aminos(sequence):
    """Zwraca listę trójek liter z sekwencji, dopuszczając jedynie trójki złożone z liter A, C, G oraz  U"""
    result = []
    current = ''
    for nucleodite in sequence:
        if len(current) < 3:
            if nucleodite not in ['A', 'C', 'G', 'U']:
                nucleodite = 'X'  # marker niepoprawnej sekwencji
            current += nucleodite
            if len(current) == 3:
                if 'X' not in current:
                    result.append(current)
                current = ''
    return result


print(dna_to_aminos('AAUAAUAAAUCAUAA') == ['AAU', 'AAU', 'AAA', 'UCA', 'UAA'])
print(dna_to_aminos('AAUAAXAAAUCAUAA') == ['AAU', 'AAA', 'UCA', 'UAA'])
print(dna_to_aminos('AAUAAYAAAUCAUAA') == ['AAU', 'AAA', 'UCA', 'UAA'])


def pairs(N):
    """ Funckja zwraca zbiór wszystkich par (x,y) dla x, y < N i x < y """
    return [(x) for x in range(0, N) if (x in range(0, N))]
    pass


print(pairs(1) == set())
print(pairs(2) == {(0, 1)})
print(pairs(3) == {(0, 1), (0, 2), (1, 2)})
print(pairs(4) == {(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)})
