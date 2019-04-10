from gingerit.gingerit import GingerIt
from autocorrect import spell
from spellchecker import SpellChecker
# from pattern.en import spelling

spel = SpellChecker(distance=3)

text = ['Downtow', 'Uber', 'Ubr pre-auth checkcark', 'Sheetz', 'Supra Payment', 'Publix', 'Hulu', 'Hlu', 'Five', 'Belo', 'Food4less']
x = 'Pymt Payroll'
parser = GingerIt()
for txt in text:
    try:
        s1 = spell(txt)
    except:
        s1 = ' NO NO NO'
    try:
        s2 = spel.correction(txt)
    except:
        s2 = ' NO NO NO'
    try:
        s3 = parser.parse(txt)
    except:
        s3 = ' NO NO NO'
    print(s1, s2, s3)


# find those words that may be misspelled
# misspelled = spell.unknown(['something', 'is', 'hapenning', 'here'])

# for word in misspelled:
#     Get the one `most likely` answer
    # print(spell.correction(word))
    #
    # Get a list of `likely` options
    # print(spell.candidates(word))