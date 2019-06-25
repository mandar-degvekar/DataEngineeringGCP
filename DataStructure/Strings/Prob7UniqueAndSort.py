inp=input('Enter strings coma separated to add in list:')
list=inp.split(',')
l=[]
for i in list:
    l.append(i)

print(l)
d=dict.fromkeys(l)
print(sorted(d))