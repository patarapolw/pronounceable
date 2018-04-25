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
2.8604533275400104
>>> complexity.complexity('a4ILot#h')
2.4983706278514015
>>> complexity.complexity('password')
1.0
>>> complexity.complexity('thisisabadpassword')
1.1620410601781446
>>> complexity.complexity('anejpwnrqpqzonijre')
2.4983706278514015
"""
import doctest
doctest.testmod()
