# -------------------------------------------------------------------------------------------------------
# https://github.com/blatinier/pyhunspell : Only for linux

# -------------------------------------------------------------------------------------------------------
# http://aspell.net/ : Linux Only





# ------------------------------------------------------------------------------------------------------
# https://en.wikipedia.org/wiki/Ispell : Linux Only
# import hunspell
# hobj = hunspell.HunSpell('/usr/share/hunspell/en_US.dic', '/usr/share/hunspell/en_US.aff')

# -------------------------------------------------------------------------------------------------------
# http://blog.macuyiko.com/post/2017/word-spellchecking-in-python.html : Works while Word is open
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

# -------------------------------------------------------------------------------------------------------
# https://github.com/rfk/pyenchant : linux only

# -------------------------------------------------------------------------------------------------------
# https://github.com/myint/scspell : NO Example given

# -------------------------------------------------------------------------------------------------------
# https://radimrehurek.com/gensim/install.html
# https://haptik.ai/tech/extract-spelling-mistakes-fasttext/

# from gensim.fasttext import FastText
#
# model = FastText.load_fasttext_format('model')
#
# print(model.wv.most_similar('recharge', topn=5))
# print(model.wv.most_similar('reminder', topn=5))
# print(model.wv.most_similar('thanks', topn=5))
# from gensim import models
#
# tfidf = models.TfidfModel(corpus)


# -------------------------------------------------------------------------------------------------------
# http://phillipmfeldman.org/English/spelling%20dictionaries.html

