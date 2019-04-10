from symspellpy.symspellpy import SymSpell, Verbosity

max_edit_distance_dictionary = 2
prefix_length = 7
check_list = ['Moxy Chicago Downtow', 'Ubr pre-auth checkcard', 'Hlu Hulu', 'Five Belo', 'Pymt Payroll', 'Sheetz', 'Supra Payment', 'Groupon', 'Publix', 'Food4less']
sym_spell = SymSpell(max_edit_distance_dictionary)

sym_spell.load_dictionary("freq_dict.txt", term_index=0, count_index=1)

max_edit_distance_lookup = 2
suggestion_verbosity = Verbosity.CLOSEST  # TOP, CLOSEST, ALL
for s in check_list:
    suggestions = sym_spell.lookup(input_term, suggestion_verbosity, max_edit_distance_lookup)
    print(suggestion)
