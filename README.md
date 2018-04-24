# Pronounceable

- Generate a random pronounceable word using Python 3 and secrets module (falls back to random module if Python < 3.6).
- Calculate password complexity based on pronounceablity. > 10 is probably too complex for human to remember.

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
16
>>> complexity.complexity('a4ILot#h')
6
```

## Based on

- https://github.com/greghaskins/gibberish
- https://github.com/ricardofalasca/passpro-generator
- NLTK - CMUdict

## More on password

- Human-readable password mnemonics -- https://github.com/patarapolw/memorable-password
- Security-side of password -- https://github.com/patarapolw/passwordstrength
- Adapting the humanized password to the computerized password policy - https://github.com/patarapolw/leetpass
