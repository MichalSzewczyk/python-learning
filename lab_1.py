# Lab

# 1.1. Funckja powinna zwrócić sume wszystkich dodatnich wieloktrotności parametru k mniejszych niż n


def sum_of_multiples(k, n=101):
    result = 0
    for i in range(2, n):
        if i % k == 0:
            result += i
    return result


print(sum_of_multiples(5) == 1050)
print(sum_of_multiples(17) == 255)
print(sum_of_multiples(69) == 69)

# 1.2. Funkcja powinna zwrócić liste liczb pierwszych mniejszych od n


def primes_less_than(n):
    primes = []
    for i in range(2, n):
        if is_relatively_prime(i, primes):
            primes.insert(len(primes), i)
    return primes


def is_relatively_prime(n, primes):
    for i in primes:
        if is_divisible(n, i):
            return False
    return True


def is_divisible(number, by):
    return number % by == 0


print(primes_less_than(5) == [2, 3])
print(primes_less_than(10) == [2, 3, 5, 7])
print(primes_less_than(20) == [2, 3, 5, 7, 11, 13, 17, 19])

# 1.3. Funkcja sprawdza czy *word* jest palindromem


def is_palindrome(word):
    return word == word[::-1]


print(is_palindrome('ala') == True)
print(is_palindrome('ananas') == False)
print(is_palindrome('ananasa') == False)
print(is_palindrome('tomek') == False)

# 1.4 Zwraca liczbę unikalnych znaków w słowie.
# Możemy założyć, że słowo składa się z małych liter alfabetu angielskiego


def how_many_different_letters(word):
    signs_occurred = []
    counter = 0
    for character in word:
        if character not in signs_occurred:
            signs_occurred.insert(0, character)
            counter += 1
    return counter


print(how_many_different_letters('tomek') == 5)
print(how_many_different_letters('ala') == 2)
print(how_many_different_letters('ananas') == 3)
print(how_many_different_letters('jola') == 4)

# 1.5. Funkcja przyjmuje 9-elementową liste i na jej podstawie tworzy stringa z HTMLową tabelą orzmiaru 3x3
#     reprezentującą plansze do gry w kółko i krzyżyk


def list_to_table(word):
    board = '<table style="table-layout: fixed; height: 90px; width: 90px;">'
    for i in range(0, 9, 3):
        board += "\n\t<tr>"
        for j in range(0, 3):
            board += "\n\t\t<td>" + word[i + j] + "</td>"
        board += "\n\t<tr>"

    board += "\n</table>"
    return board


print(list_to_table(['X', '', 'O', '', 'X', '', 'O', '', 'O']))


# Oczekiwany wynik:
# X		O
#     X
# O		O


# Extra exercise:

# 1.6. Napisz definicję funkcji HowManyIntegers(N), która zwróci jak wiele liczb
# z zakresu [1,N) składa się wyłącznie z cyfr {0,2,7,9}.


def how_many_integers_normal(number, allowed_digits):
    counter = 0
    for i in range(1, number):
        number_converted_to_string = str(i)
        for character in number_converted_to_string:
            if int(character) not in allowed_digits:
                counter -= 1
                break
        counter += 1
    return counter

# short version: 94 chars


def how_many_integers(n, d):
    r = 0
    for i in range(1, n):
        for c in str(i):
            if int(c) not in d:
                r -= 1
                break
        r += 1
    return r

digits = [0, 2, 7, 9]
print(how_many_integers(1, digits) == 0)
print(how_many_integers(10, digits) == 3)  # 2,7,9
print(how_many_integers(28, digits) == 6)  # 2,7,9,20,22,27
