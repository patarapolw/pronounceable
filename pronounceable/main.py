try:
    from secrets import randbelow as randrange
    from secrets import choice
except ImportError:
    from random import randrange, choice

from pronounceable.digraph import DIGRAPHS_FREQUENCY
from pronounceable.components import INITIAL_CONSONANTS, FINAL_CONSONANTS, double_vowels


class PronounceableWord:
    """
    Based on https://github.com/ricardofalasca/passpro-generator, but in Python 3

        Generate pronounceable passwords
        This module generates pronounceable passwords, based the the English
        digraphs by D Edwards.
        History
        --
        This code derived from Perl module: Text::Password::Pronounceable,
        written by Ricardo Falasca <ricardo at falasca.com.br> published
        under MIT License.
        Python library by `Ricardo Falasca (MyCanadaPayday.com)`, 2018-04-03.
        That was derived from mpw.pl, a bit of code with a sordid history.
        CPAN module by Chia-liang Kao, 2006-09-11.
        Perl cleaned up a bit by Jesse Vincent, 2001-01-14.
        Converted to perl from C by Marc Horowitz, 2000-01-20.
        Converted to C from Multics PL/I by Bill Sommerfeld, 1986-04-21.
        Original PL/I version provided by Jerry Saltzer.
    """

    # Default min and max length
    min_length = 6
    max_length = 10

    # We need to know the totals for each row
    row_sums = [sum(f) for f in DIGRAPHS_FREQUENCY]

    # Frequency with which a given letter starts a word.
    start_freq = [
        1299, 425, 725, 271, 375, 470, 93, 223, 1009, 24, 20, 355, 379, 319,
        823, 618, 21, 317, 962, 1991, 271, 104, 516, 6, 16, 14
    ]

    total_sum = sum(start_freq)

    def _check_lengths(self, min_length, max_length):
        if not min_length:
            return 'Min length should be defined'
        elif min_length <= 0:
            return 'Min length should be > 0'

        if not max_length:
            return 'Max length should be defined'
        elif max_length <= 0:
            return 'Max length should be > 0'

        if min_length > max_length:
            return 'Max length must be >= min length'

    def length(self, min_length, max_length):
        """

        :param min_length:
        :param max_length:
        :return:
        >>> Pronounceable().length(6, 10)
        'centte'
        """
        min_length = min_length or self.min_length
        max_length = max_length or self.max_length

        if not min_length and not max_length:
            return

        # When munging characters, we need to know where to start counting
        # letters from
        length = min_length + randrange(max_length - min_length)
        char = self._generate_nextchar(self.total_sum, self.start_freq)
        a = ord('a')
        word = chr(char + a)

        for i in range(1, length):
            char = self._generate_nextchar(self.row_sums[char],
                                           DIGRAPHS_FREQUENCY[char])
            word += chr(char + a)
        return word

    # A private helper function for RandomPassword
    # Takes a row summary and a frequency chart for the next character to be
    # searched
    def _generate_nextchar(self, all, freq):
        i, pos = 0, randrange(all)

        while i < (len(freq) - 1) and pos >= freq[i]:
            pos -= freq[i]
            i += 1

        return i


def generate_word():
    """

    :return: str
    >>> generate_word()

    """
    return choice(INITIAL_CONSONANTS) \
           + choice(choice(['aeiouy', list(double_vowels())])) \
           + choice(['', choice(FINAL_CONSONANTS)])


if __name__ == '__main__':
    pass
