inp=input('Enter strings coma separated to add in list:')
list=inp.split(',')
l=[]
for i in list:
    l.append(i)

print(l)
largestval=l[0]
lenoflar=len(largestval)
print(max(l),'length=',len(max(l)))
# for i in l:
#     if len(i) > lenoflar:
#          largestval=len(i)
# print(largestval,' length:',len(largestval))
