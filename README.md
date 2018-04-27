# Pronounceable

[![Build Status](https://travis-ci.org/patarapolw/pronounceable.svg?branch=master)](https://travis-ci.org/patarapolw/pronounceable)
[![PyPI version shields.io](https://img.shields.io/pypi/v/pronounceable.svg)](https://pypi.python.org/pypi/pronounceable/)
[![PyPI license](https://img.shields.io/pypi/l/pronounceable.svg)](https://pypi.python.org/pypi/pronounceable/)

- Generate a random pronounceable word using Python 3 and secrets module (falls back to random module if Python < 3.6).
- Calculate password complexity based on pronounceablity. > 10.0 is probably too complex for human to remember.

## Usage

```pycon
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
```

## Based on

- https://github.com/greghaskins/gibberish
- https://github.com/ricardofalasca/passpro-generator
- NLTK - CMUdict

## More on password

- Human-readable password mnemonics -- https://github.com/patarapolw/memorable-password
- Security-side of password -- https://github.com/patarapolw/passwordstrength
- Adapting the humanized password to the computerized password policy - https://github.com/patarapolw/leetpass
