"""
Initial and final consonants from https://github.com/greghaskins/gibberish
"""
import string

from pronounceable.digraph import DIGRAPHS_FREQUENCY

INITIAL_CONSONANTS = list(set(string.ascii_lowercase) - set('aeiou')
                          # remove those easily confused with others
                          - set('qxc')
                          # add some crunchy clusters
                          | {'bl', 'br', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl', 'gr', 'pl', 'pr', 'sk', 'sl', 'sm', 'sn',
                             'sp', 'st', 'str', 'sw', 'tr', 'ch', 'sh'}
                          )

FINAL_CONSONANTS = list(set(string.ascii_lowercase) - set('aeiou')
                        # remove the confusable
                        - set('qxcsj')
                        # crunchy clusters
                        | {'ct', 'ft', 'mp', 'nd', 'ng', 'nk', 'nt', 'pt', 'sk', 'sp', 'ss', 'st', 'ch', 'sh'}
                        )


def all_consonants():
    # single consonants
    for a in set(string.ascii_lowercase) - set('aeiou'):
        yield a

    # double consonants
    for ia, a in enumerate(string.ascii_lowercase):
        for ib, b in enumerate(string.ascii_lowercase):
            if DIGRAPHS_FREQUENCY[ib][ia] > 0:
                if b not in 'aeiou' and a not in 'aeiouy':
                    yield (b + a)


def double_vowels():
    for ia, a in enumerate(string.ascii_lowercase):
        for ib, b in enumerate(string.ascii_lowercase):
            if DIGRAPHS_FREQUENCY[ib][ia] > 0:
                if a in 'aeiou' and b in 'aeiou':
                    yield (a + b)


if __name__ == '__main__':
    pass
