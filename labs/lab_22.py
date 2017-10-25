# zad 1
""" Sprawdza czy podane słowa są anagramami """


def check_anagram_simple(first, second):
    return prepare_for_comparison(first) == prepare_for_comparison(second)


def prepare_for_comparison(word: str):
    return sorted(word.replace(' ', '').lower())


print(check_anagram_simple("abcd", "dcba") == True)
print(check_anagram_simple("aba", "baa") == True)
print(check_anagram_simple("aba", "ba") == False)
print(check_anagram_simple("tom marvolo riddle ", "i am lord voldemort") == True)


def check_anagram_faster(first, second):
    d = {}
    if len(first) != len(second):
        return False
    for character in first.replace(' ', '').lower():
        if character in d:
            d[character] += 1
        else:
            d[character] = 1

    for character in second.replace(' ', '').lower():
        if character not in d:
            return False
        elif d[character] is 0:
            return False
        else:
            d[character] -= 1
    return True


print(check_anagram_faster("abcd", "dcba") == True)
print(check_anagram_faster("aba", "baa") == True)
print(check_anagram_faster("aba", "ba") == False)
print(check_anagram_faster("tom marvolo riddle ", "i am lord voldemort") == True)


# zad 2
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


# zad 3
def even_numbers_from_list(data):
    """Zwraca podlistę "data" zawierającą wyłącznie parzyste liczby"""
    return [x for x in data if x % 2 == 0]


print(even_numbers_from_list([1, 2, 3, 4]) == [2, 4])
print(even_numbers_from_list(range(10)) == list(range(0, 10, 2)))
print(even_numbers_from_list(range(1000)) == list(range(0, 1000, 2)))
print(even_numbers_from_list([10, 2, 3, 4, 6, -3, -4]) == [10, 2, 4, 6, -4])


# zad 4
def words_analyze(words):
    """Zwraca listę trójek, gdzie i'ta trójka to (i, i'te słowo, długość i'tego słowa)"""
    return [(ind, x, len(x)) for ind, x in enumerate(words)]


print(words_analyze(['tomek', 'jadzia']) == [(0, 'tomek', 5), (1, 'jadzia', 6)])
print(words_analyze([]) == [])


# zad 5
def count_words_starting_with_letter(text, letter):
    """Zwraca słownik gdzie kluczami są wszystkie słowa występujące w tekście
    rozpoczynające się na zadaną literę, a wartością ile razy wystąpiy"""
    return {value: text.split(' ').count(value) for value in text.split(' ') if value[0] == letter}


print(count_words_starting_with_letter('ola ma kota o imieniu ola', 'o') == {'ola': 2, 'o': 1})
print(count_words_starting_with_letter('ola ma kota o imieniu ola', 'k') == {'kota': 1})
print(count_words_starting_with_letter('ola ma kota o imieniu ola', 'x') == {})


# zad 5
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


# zad 6
def dna_to_aminos_single_line(sequence):
    return [sequence[3 * index] + sequence[3 * index + 1] + sequence[3 * index + 2]
            for (index, x) in enumerate(sequence[::3])
            if sequence[3 * index] in ['A', 'C', 'G', 'U'] and
            sequence[3 * index + 1] in ['A', 'C', 'G', 'U'] and
            sequence[3 * index + 2] in ['A', 'C', 'G', 'U']]


print(dna_to_aminos_single_line('AAUAAUAAAUCAUAA') == ['AAU', 'AAU', 'AAA', 'UCA', 'UAA'])
print(dna_to_aminos_single_line('AAUAAXAAAUCAUAA') == ['AAU', 'AAA', 'UCA', 'UAA'])
print(dna_to_aminos_single_line('AAUAAYAAAUCAUAA') == ['AAU', 'AAA', 'UCA', 'UAA'])


# zad 7
def pairs(N):
    """ Funckja zwraca zbiór wszystkich par (x,y) dla x, y < N i x < y """
    return {(x, y) for x in range(N) for y in range(N) if x < y < N}


print(pairs(1) == set())
print(pairs(2) == {(0, 1)})
print(pairs(3) == {(0, 1), (0, 2), (1, 2)})
print(pairs(4) == {(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)})

# zad 8

import time
from math import sqrt


def primes(N):
    return {x for x in range(2, N + 1) if all(x % y for y in range(2, int(sqrt(x)) + 1))}


print(primes(5) == {2, 3, 5})
print(primes(10) == {2, 3, 5, 7})
print(primes(100) == {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97})
start = time.time()
primes(1000)
length = time.time() - start
print(primes(100000))


def primes_extra_A(N):
    """Zwraca zbiór liczb pierwszych od 0 do N włącznie"""
    return {x for x in custom_range(2, N + 1) if all(x % y for y in custom_range(2, int(sqrt(x)) + 1))}


def custom_range(start, end):
    if start is not end:
        yield from custom_range(start + 1, end)
        yield start


print(primes_extra_A(5) == {2, 3, 5})
print(primes_extra_A(10) == {2, 3, 5, 7})
print(
    primes_extra_A(100) == {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
                            97})


def primes_extra_B(N):
    """Zwraca zbiór liczb pierwszych od 0 do N włącznie"""
    # return {x for x in range(2, N + 1) if all(x % y for y in range(2, int(sqrt(x)) + 1))}
    # return map(lambda x,y: x+y, range(2, N + 1))
    return map(lambda x: filter(lambda y: x % y == 0, range(2, int(sqrt(x)) + 1)), range(2, N + 1))


# return map(lambda x,y: x+y, range(2, N + 1))
print(primes_extra_B(5))
print(primes_extra_B(5) == {2, 3, 5})
print(primes_extra_B(10) == {2, 3, 5, 7})
print(
    primes_extra_B(100) == {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
                            97})
