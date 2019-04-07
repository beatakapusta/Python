"Laboratorium 4, Beata Kapusta"

import codecs, re

# Zadanie 4.1

def invert(in_filename, out_filename):
    "Odwraca zawartość pliku tekstowego."
    input_file  = open(in_filename, 'r', encoding='utf8')
    output_file = open(out_filename, 'w', encoding='utf8')

    # uzupełnij

    for line in reversed(input_file.readlines()):
         output_file.write(line[::-1])

    input_file.close()
    output_file.close()

invert('inverted.txt', 'wiki10.txt')

# Zadanie 4.2

def unique_words(filename):
    "Zwraca posortowaną alfabetycznie listę wszystkich słów z pliku."

    def _words_from_line(line):
        "Zwraca listę słów dla linijki tekstu unicode."
        words = re.split('[\W\d]+', line)
        return [w.lower() for w in words if w]

    wordset = set()

    f = open(filename, 'r', encoding="utf8")
    for line in f:
        words = _words_from_line(line)
        for word in words:
            wordset.add(word)
    f.close()

    return sorted(list(wordset))

print('Zadanie 4.2\n Wszystkie słowa z pliku wiki.txt:\n', unique_words('wiki10.txt'))

# Zadanie 4.3

def word_stat(filename):
    '''
    Zwraca posortowaną malejąco statystykę wystąpień słów
    w pliku w postaci listy par (słowo, liczba).
    '''
    def _words_from_line(line):
        "Zwraca listę słów dla linijki tekstu unicode."
        words = re.split('[\W\d]+', line)
        return [w.lower() for w in words if w]

    def _sort_stat(stat):
        "Sortuje malejąco listę par według drugiego elementu."
        return sorted(stat, key=lambda p: p[1], reverse=True)

    #uzupełnij
    d = dict()
    n = 1

    f = open(filename, 'r', encoding="utf8")
    for line in f:
        words = _words_from_line(line)
        for word in words:
            if word in d.keys():
                d[word] = d[word]+1
            else:
                d[word] = n


    result = list(d.items())
    return _sort_stat(result)

print('Zadanie 4.3\n Posortowana malejąco statystyka wystąpień słów w pliku wiki.txt:\n', word_stat('wiki10.txt'))

# Funkcje pomocnicze

def _words_from_line(line):
    "Zwraca listę słów dla linijki tekstu unicode."
    words = re.split('[\W\d]+', line)
    return [w.lower() for w in words if w]

def _sort_stat(stat):
    "Sortuje malejąco listę par według drugiego elementu."
    return sorted(stat, key=lambda p: p[1], reverse=True)
