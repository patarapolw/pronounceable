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


def test_rareness_random(length=30):
    """

    :param length:
    :return:
    length=10: 0.0098 seconds per test_complexity_random
    length=20: 0.4591 seconds per test_complexity_random
    length=30: 29.8628 seconds per test_complexity_random
    """
    word = ''.join([choice(string.ascii_lowercase) for _ in range(length)])
    print(word, c.rareness(word))


def test_complexity_pronounceable(min_length=8, max_length=12):
    """

    :param min_length:
    :param max_length:
    :return:
    """
    word = pr.length(min_length, max_length)
    print(word, c.complexity(word))


def test_complexity_garble():
    """

    :return:
    """
    word = generate_word()
    print(word, c.complexity(word))


if __name__ == '__main__':
    from tests import timeit

    timeit(test_rareness_random)
