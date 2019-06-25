from operator import itemgetter
l=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sorted(l,key=itemgetter(1)))


