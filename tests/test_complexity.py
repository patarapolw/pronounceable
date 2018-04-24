"""
1.5280 seconds per Pronounceablity
1.5301 seconds per Complexity
"""
import string
from random import choice

from pronounceable.complexity import Complexity, Pronounceablity
from pronounceable import PronounceableWord, generate_word

pr = PronounceableWord()
c = Complexity()


def test_complexity_random(length=10):
    """

    :param length:
    :return:
    Pronounceablity.syllable: 5-9
    """
    word = ''.join([choice(string.ascii_lowercase) for _ in range(length)])
    print(word, c.complexity(word))


def test_complexity_pronounceable(min_length=8, max_length=12):
    """

    :param min_length:
    :param max_length:
    :return:
    Pronounceablity.syllable: 4-6
    """
    word = pr.length(min_length, max_length)
    print(word, c.complexity(word))


def test_complexity_garble():
    """

    :return:
    Pronounceablity.syllable: 1-4
    """
    word = generate_word()
    print(word, c.complexity(word))


if __name__ == '__main__':
    from tests import timeit

    timeit(test_complexity_garble)
