# Install sympound, pyxdameraulevenshtein

from sympound import sympound
import platform

distancefun = None
if platform.system() != "Windows":
    from pyxdameraulevenshtein import damerau_levenshtein_distance
    distancefun = damerau_levenshtein_distance
else:
    from jellyfish import jaro_winkler 
    distancefun = jaro_winkler


check_list = ['Moxy','Moxy Chicago Downtow', 'Ubr pre-auth checkcard', 'Hlu Hulu', 'Five Belo', 'Pymt Payroll', 'Sheetz', 'Supra Payment', 'Groupon', 'Publix', 'Food4less']

ssc = sympound(distancefun=distancefun, maxDictionaryEditDistance=4)


ssc.load_dictionary("freq_dict.txt", term_index=0, count_index=1)
##ssc.load_pickle("symspell.pickle")
for s in check_list:
    print(ssc.lookup_compound(input_string=s, edit_distance_max=2))


ssc.save_pickle("symspell.pickle")
##ssc.load_pickle("symspell.pickle")
