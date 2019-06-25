duptup=('a','b','a','c','d','b','e','e')
s=set()
count=0
print(duptup)
for i in duptup:
    if duptup.count(i) > 1:
        s.add(i)


print('duplicate')
print(s)