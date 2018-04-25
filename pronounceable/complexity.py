from metaphone import doublemetaphone
from nltk.corpus import cmudict
import yaml
import string

from pronounceable.dir import database_path


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
        if common_words is None:
            with open(database_path('google-10000-english.txt')) as f:
                self.common_words = f.read().strip().split('\n')
        else:
            self.common_words = common_words
        super().__init__(leet)

    def absolute_complexity(self, password):
        return (2 * self.non_char(password)
                + self.syllable(password)
                + 5 * (1 - self.consecutiveness(password))
                + 10 * (1 - self.commonness(password))
                # + len(password)
                )

    def complexity(self, password, relative_to='password'):
        return self.absolute_complexity(password) / self.absolute_complexity(relative_to)

    def commonness(self, password, min_word_fragment_length=3):
        """

        :param password:
        :param int min_word_fragment_length:
        :return int: in range 0-1
        >>> Complexity().commonness('helloworld')
        0.7304599999999999
        """
        def recurse_keyword(i_depth):
            nonlocal depth, keywords

            for i_depth_1 in range(i_depth - min_word_fragment_length*depth):
                if depth < n:
                    depth += 1
                    keywords.add(password[i_depth_1:i_depth].lower())
                    recurse_keyword(i_depth_1)
                else:
                    keywords.add(password[0:i_depth].lower())

        keywords = set()
        for n in range(len(password)//min_word_fragment_length):
            for i_n_1 in range(len(password)):
                depth = 1
                keywords.add(password[i_n_1:].lower())
                recurse_keyword(i_n_1)

        commonness_list = []
        for keyword in keywords:
            if keyword in self.common_words:
                commonness_list.append(1 - (self.common_words.index(keyword) / 10000))

        if len(commonness_list) > 0:
            return sum(commonness_list)/len(commonness_list)
        else:
            return 0

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
        """
        consec = 0
        for i in range(len(password) - consecutive_length):
            if all([char.islower() for char in password[i:i+consecutive_length]]):
                consec += 1
            elif all([char.islower() for char in password[i:i+consecutive_length]]):
                consec += 1

        return consec / (len(password) - consecutive_length)

    @staticmethod
    def non_char(password):
        n = 0
        for char in password:
            if char not in string.ascii_letters:
                n += 1

        return n


if __name__ == '__main__':
    c = Complexity()
    print(c.complexity('password'))
