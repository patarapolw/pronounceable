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
>>> complexity = Complexity()
>>> complexity.complexity('D7!rcc&umnsd')
6
>>> complexity.complexity('a4ILot#h')
4
"""
import doctest
doctest.testmod()
