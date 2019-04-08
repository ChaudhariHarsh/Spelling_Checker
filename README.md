# Spelling Checker Libraries & Code.

> ## This repository is for finding best Spell Checking and find.

 
## [GingerIt](https://github.com/Azd325/gingerit) : 

> pip install gingerit

```
from gingerit.gingerit import GingerIt

text = 'The smelt of fliwers bring back memories.'

parser = GingerIt()
parser.parse(text)
```

## [Autocorrect](https://github.com/phatpiglet/autocorrect) : 

> pip install autocorrect

```
from autocorrect import spell
spell('HTe')
```

## [Pyspellchecker](https://pypi.org/project/pyspellchecker/) : 

> pip install pyspellchecker

```
from spellchecker import SpellChecker

spell = SpellChecker()

misspelled = spell.unknown(['something', 'is', 'hapenning', 'here'])

for word in misspelled:
    print(spell.correction(word))

    print(spell.candidates(word))
```

## [Pattern](https://www.clips.uantwerpen.be/pages/pattern-en) : 

> pip install pattern

```
from pattern.web import Twitter
from pattern.en import tag
from pattern.vector import KNN, count

twitter, knn = Twitter(), KNN()

for i in range(1, 3):
    for tweet in twitter.search('#win OR #fail', start=i, count=100):
        s = tweet.text.lower()
        p = '#win' in s and 'WIN' or 'FAIL'
        v = tag(s)
        v = [word for word, pos in v if pos == 'JJ'] # JJ = adjective
        v = count(v) # {'sweet': 1}
        if v:
            knn.train(v, type=p)

print(knn.classify('sweet potato burger'))
print(knn.classify('stupid autocorrect'))
```

## [Symspell](https://github.com/mammothb/symspellpy) : 

> pip install -U symspellpy

```
import os

from symspellpy.symspellpy import SymSpell  # import the module

def main():
    # maximum edit distance per dictionary precalculation
    max_edit_distance_dictionary = 2
    prefix_length = 7
    # create object
    sym_spell = SymSpell(max_edit_distance_dictionary, prefix_length)
    
    # create dictionary using corpus.txt
    if not sym_spell.create_dictionary(<path/to/corpus.txt>):
        print("Corpus file not found")
        return

    for key, count in sym_spell.words.items():
        print("{} {}".format(key, count))

if __name__ == "__main__":
    main()
```

## [Sympound](https://pypi.org/project/sympound/) : 

> pip install sympound

```
from gingerit.gingerit import GingerIt

text = 'The smelt of fliwers bring back memories.'

parser = GingerIt()
parser.parse(text)
```

## [Peter-Norvig code](http://norvig.com/spell-correct.html) : 

> Its just code.

```
import re
from collections import Counter

def words(text): return re.findall(r'\w+', text.lower())

WORDS = Counter(words(open('big.txt').read()))

def P(word, N=sum(WORDS.values())): 
    "Probability of `word`."
    return WORDS[word] / N

def correction(word): 
    "Most probable spelling correction for word."
    return max(candidates(word), key=P)

def candidates(word): 
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

def known(words): 
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)

def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))
```
## [Win32com - Word Application](http://blog.macuyiko.com/post/2017/word-spellchecking-in-python.html) : 

> pip install pywin32

```
http://blog.macuyiko.com/post/2017/word-spellchecking-in-python.html : Works while Word is open
import win32com.client

text = 'speling'
language = 1033
word = win32com.client.Dispatch('Word.Application')
word.Visible = True
wordDoc = word.Documents.Add()
wordDoc.Range().LanguageID = language
wordDoc.Range().Text = text
corrections = {'spelling': [],
               'grammar': [],
               'spellingcount': 0,
               'grammarcount': 0,
               'text': text}
def rng_to_dict(rng):
    d = {'text': rng.Text, 'start': rng.Start, 'end': rng.End, 'suggestions': []}
    for i in range(1, rng.GetSpellingSuggestions().Count+1):
        d['suggestions'].append(rng.GetSpellingSuggestions().Item(i).Name)
    return d
for rng in wordDoc.Range().SpellingErrors:
    corrections['spelling'].append(rng_to_dict(rng))
    corrections['spellingcount'] += 1
for rng in wordDoc.Range().GrammaticalErrors:
    corrections['grammar'].append(rng_to_dict(rng))
    corrections['grammarcount'] += 1
print(corrections['grammar'][0]['suggestions'][0])
wordDoc.Close()
word.Quit()
```
## [Hunspell](https://github.com/blatinier/pyhunspell) : 

> pip install hunspell

```
import hunspell
hobj = hunspell.HunSpell('/usr/share/hunspell/en_US.dic', '/usr/share/hunspell/en_US.aff')
hobj.spell('spookie')
```
## [Ispell](http://code.activestate.com/recipes/117221-spell-checking/) : 

> Its Code

```
Not yet tested
```
## [Aspell](http://aspell.net/) : 

> pip install aspell-python-py3

```
Not yet tested
```

## [Pyenchant](https://github.com/rfk/pyenchant) : 

> pip install pyenchant

```
Not yet tested
```
## [Scspell](https://github.com/myint/scspell) : 

> pip install scspell3k

```
Not yet tested
```
## [Gensim](https://radimrehurek.com/gensim/install.html) : 

> pip install --upgrade gensim

```
from gensim import models, similarities

tfidf = models.TfidfModel(corpus)
index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=12)
sims = index[tfidf[vec]]
print(list(enumerate(sims)))
```

