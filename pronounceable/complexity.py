from metaphone import doublemetaphone
from nltk.corpus import cmudict
import yaml

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
        upper = ''
        lower = ''
        non_char = ''
        for char in password:
            if char.isupper():
                upper += char
            elif char.islower():
                lower += char
            else:
                non_char += char

        return abs(len(upper) - len(lower)) - min([len(upper), len(lower)]) \
               + len(non_char) \
               + self.syllable(password)


if __name__ == '__main__':
    c = Complexity()
    print(c.syllable('hello'))
