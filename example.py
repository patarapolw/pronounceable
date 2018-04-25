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
2.109245301020895
>>> complexity.complexity('a4ILot#h')
1.5255462265051045
>>> complexity.complexity('password')
1.0
"""
import doctest
doctest.testmod()
