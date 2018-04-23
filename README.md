# Pronounceable

Generate a random pronounceable word using Python 3 and secrets module (falls back to random module if Python < 3.6).

## Usage

```pydocstring
>>> from pronounceable import Pronounceable, generate_word
>>> Pronounceable().length(8, 15)
'terhtsadathe'
>>> generate_word()
'gloust'
```

## Based on

https://github.com/greghaskins/gibberish

https://github.com/ricardofalasca/passpro-generator
