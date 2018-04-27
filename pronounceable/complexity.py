from metaphone import doublemetaphone
from nltk.corpus import cmudict
import yaml
import string
import math

from pronounceable.dir import database_path

__doctest_skip__ = ['Complexity.rareness2']


def possible_syllables():
    d = cmudict.dict()
    for word in d.keys():
        for pron in d[word]:
            for phone in pron:
                yield phone


class Pronounceablity:
    def __init__(self, leet=None):
        """

        :param dict leet: leet substitutions
        """
        self.possible_syllables = sorted(set(possible_syllables()), key=len, reverse=True)
        self.substitution = dict()
        if leet is not None:
            for k, v in leet.items():
                for symbol in v:
                    self.substitution.setdefault(symbol, []).append(k)

    def syllable(self, word):
        clean_word = ''
        for char in word:
            clean_word += self.substitution.get(char, [char])[0]

        phone = doublemetaphone(clean_word)[0]
        for syllable in self.possible_syllables:
            phone = phone.replace(syllable, '@')

        return len(phone)


class Complexity(Pronounceablity):
    def __init__(self, leet=None, common_words=None):
        """

        :param dict leet: a dictionary containing leet substitutions (see leetspeak.yaml)
        :param list common_words: a list containing common words, sorted by commonness
        """
        if leet is None:
            with open(database_path('leetspeak.yaml')) as f:
                leet = yaml.safe_load(f)['min']
        self.common_words = dict()
        if common_words is None:
            with open(database_path('google-10000-english.txt')) as f:
                for i, row in enumerate(f):
                    self.common_words[row.strip()] = i
        else:
            for i, word in enumerate(common_words):
                self.common_words[word] = i
        super().__init__(leet)

    def absolute_complexity(self, password):
        return (2 * self.non_char(password)
                + self.syllable(password)
                + 5 * (1 - self.consecutiveness(password))
                + 10 * self.rareness(password)
                # + len(password)
                )

    def complexity(self, password, relative_to='password'):
        return self.absolute_complexity(password) / self.absolute_complexity(relative_to)

    def rareness(self, password, min_word_fragment_length=3, absolute_rareness_cutoff=0.1):
        """

        :param password:
        :param int min_word_fragment_length:
        :param float absolute_rareness_cutoff:
        :return int: in range 0-1
        >>> Complexity().rareness('thethethe')
        0.0
        >>> Complexity().rareness('poison')  # the last word in Google's list
        0.19649219348046737
        >>> Complexity().rareness('asdfegu')
        1
        >>> Complexity().rareness('helloworld')
        0.1644235716987842

        # Good words should eval less than 0.2
        >>> Complexity().rareness('verylongpassword')
        0.16626577386889024
        >>> Complexity().rareness('averylongpassword')
        0.1622989831750065
        >>> Complexity().rareness('ultrasupersuperlonglonglongpasswordlongerthanlonger')
        0.23084370223197

        # Half gibberish should not eval 1
        >>> Complexity().rareness('ultrasuperlongpasswordsdhsdhjksdskdhskjdhakdhsadjdi')
        0.40519672587970423

        # Gibberish of various length should eval approx. 1
        >>> Complexity().rareness('faxwyhxihs')
        1
        >>> Complexity().rareness('aarhzcrzncseexdeccli')
        1
        >>> Complexity().rareness('qdhlivjpyyobhowxixzgupdhdsmzeu')
        1
        >>> Complexity().rareness('jjvkzlrjtraszzxrrztyrjhytvdjvvgujelareztwlkpuwutfw')
        1
        """
        sub_words = list()
        for i_front in range(0, len(password) - min_word_fragment_length + 1):
            for i_back in range(i_front + min_word_fragment_length, len(password) + 1):
                sub_words.append(password[i_front:i_back])

        all_valid_com = set()
        total_sub_word_length = 0
        for sub_word in sub_words:
            try:
                all_valid_com.add(self.common_words[sub_word] / len(sub_word))
                total_sub_word_length += len(sub_word)
            except KeyError:
                pass

        try:
            absolute_rareness = (((sum(all_valid_com, 0)/len(all_valid_com)) / len(self.common_words))
                                 * (len(sub_words) / total_sub_word_length**2)
                                 * (len(password) / total_sub_word_length))
            # return absolute_rareness
            return math.sqrt(absolute_rareness/absolute_rareness_cutoff) \
                if absolute_rareness < absolute_rareness_cutoff else 1
        except ZeroDivisionError:
            return 1

    def rareness2(self, password, min_word_fragment_length=3, commonness_of_non_word=50000):
        """
        A logical way to calculate rareness, but the speed is illogical for length > 40.
        (length 45: 60 sec per test)

        :param password:
        :param int min_word_fragment_length:
        :param int commonness_of_non_word: an arbitrary value to improve commonness of 'poison'
        :return int: in range 0-1
        >>> Complexity().rareness2('thethethe')
        0.0
        >>> Complexity().rareness2('poison')  # the last word in Google's list
        0.19998
        >>> Complexity().rareness2('asdfegu')
        1
        >>> Complexity().rareness2('helloworld')
        0.02537
        >>> Complexity().rareness2('verylongpassword')
        0.006806666666666667
        >>> Complexity().rareness2('averylongpassword')
        0.26282000000000005
        >>> Complexity().rareness2('djkhsdjkashdaslkdhas')
        0.31674
        """
        from time import time

        def get_min_commonness_value(commonness_list):
            nonlocal commonness_value

            value = sum(commonness_list)/len(commonness_list)
            if value < commonness_value:
                commonness_value = value

        def recurse(previous):
            nonlocal separators, depth, used_separators
            depth += 1

            for current in range(previous + min_word_fragment_length, len(password) - min_word_fragment_length + 1):
                try:
                    separators[depth] = current
                except IndexError:
                    separators.append(current)

                if depth < number_of_separators - 1:
                    recurse(current)
                else:
                    used_separators.add(tuple(separators))

            depth -= 1

        start = time()
        subword_commonness = dict()
        for i_front in range(0, len(password) - min_word_fragment_length + 1):
            for i_back in range(i_front + min_word_fragment_length, len(password) + 1):
                subword_commonness[(i_front, i_back)] \
                    = self.common_words.get(password[i_front:i_back], commonness_of_non_word)/commonness_of_non_word
        print('subword complete', time()-start)

        start = time()
        commonness_value = 1
        used_separators = set()
        for number_of_separators in range(len(password)//min_word_fragment_length):
            if number_of_separators == 0:
                get_min_commonness_value\
                    ({self.common_words.get(password, commonness_of_non_word)/commonness_of_non_word})
            else:
                separators = list()
                depth = -1
                recurse(0)
        print('tuple listing complete', time()-start)

        start = time()
        for sep in used_separators:
            commonness_list = set()
            commonness_list.add(subword_commonness[(0, sep[0])])
            for i in range(len(sep)-1):
                commonness_list.add(subword_commonness[(sep[i], sep[i + 1])])
            commonness_list.add(subword_commonness[(sep[-1], len(password))])
            get_min_commonness_value(commonness_list)
        print('get min complete', time()-start)

        return commonness_value

    @staticmethod
    def consecutiveness(password, consecutive_length=3):
        """
        Consecutiveness is the enemy of entropy, but makes it easier to remember.
        :param str password:
        :param int consecutive_length: length of the segment to be uniform to consider loss of entropy
        :param int base_length: usual length of the password
        :return int: in range 0-1
        >>> Complexity.consecutiveness('password')
        1.0
        >>> Complexity.consecutiveness('PaSsWoRd')
        0.0
        >>> Complexity.consecutiveness('yio')
        0
        """
        consec = 0
        for i in range(len(password) - consecutive_length):
            if all([char.islower() for char in password[i:i+consecutive_length]]):
                consec += 1
            elif all([char.islower() for char in password[i:i+consecutive_length]]):
                consec += 1

        try:
            return consec / (len(password) - consecutive_length)
        except ZeroDivisionError:
            return 0

    @staticmethod
    def non_char(password):
        n = 0
        for char in password:
            if char not in string.ascii_letters:
                n += 1

        return n


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    # Complexity().rareness('helloworld')
