"""
A template for the Words assignment.
"""
from __future__ import print_function


def average_length_of_words():
    ln = 0
    res = 0
    with open('twl06.txt') as f:
        for w in f:
            ln += 1
            res += len(w.strip())
    return res / ln


def count_occurences(character):
    res = 0
    with open('twl06.txt') as f:
        for w in f:
            for c in w:
                if c == character:
                    res += 1
    return res


if __name__ == "__main__":
    print(average_length_of_words())
    print(count_occurences("a"))
