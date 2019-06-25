s='mandar'
d=dict.fromkeys(s)
for key in d:
    d[key]=0
print(d)
for i in s:
    for key in d:
        if(key==i):
            d[key]=d[key]+1

print(d)



