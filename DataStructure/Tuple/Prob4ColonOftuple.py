from copy import deepcopy
tup = ("HELLO", 5, [], True)
print(tup)
tuplex_colon = deepcopy(tup)
tuplex_colon[2].append(12)
print(tuplex_colon)