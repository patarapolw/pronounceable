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
    def __init__(self, leet=None):
        if leet is None:
            with open(database_path('leetspeak.yaml')) as f:
                leet = yaml.safe_load(f)['min']
        super().__init__(leet)

    def complexity(self, password):
        return self.non_char(password) \
               + self.syllable(password) \
               - self.consecutiveness(password)

    @staticmethod
    def consecutiveness(password):
        """
        Consecutiveness is the enemy of entropy, but makes it easier to remember.
        :param password:
        :return:
        """
        consec = 0
        for i in range(len(password) - 3):
            if all([char.islower() for char in password[i:i+3]]):
                consec += 1
            elif all([char.islower() for char in password[i:i+3]]):
                consec += 1

        return consec

    @staticmethod
    def non_char(password):
        n = 0
        for char in password:
            if char not in string.ascii_letters:
                n += 1

        return n


if __name__ == '__main__':
    c = Complexity()
    print(c.syllable('hello'))
