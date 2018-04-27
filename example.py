"""
>>> from pronounceable import PronounceableWord, generate_word, Pronounceablity, Complexity
>>> PronounceableWord().length(8, 15)
'terhtsadathe'
>>> generate_word()
'gloust'
>>> pr = Pronounceablity()
>>> pr.syllable('terhtsadathe')
6
>>> pr.syllable('hello')
2
>>> pr.syllable('gloust')
4
>>> complexity = Complexity()
>>> complexity.complexity('D7!rcc&umnsd')
5.401603904395188
>>> complexity.complexity('a4ILot#h')
4.71785657472491
>>> complexity.complexity('password')
1.0
>>> complexity.complexity('thisisabadpassword')
2.2220669581020354
>>> complexity.complexity('anejpwnrqpqzonijre')
4.71785657472491
"""
import doctest
doctest.testmod()

__doctest_skip__ = ['*']
