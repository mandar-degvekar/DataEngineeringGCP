Dic={3:'mandar',4:'Ankita',1:'Nagesh',2:'rahul'}
print(Dic)
print('asc')
for key in sorted(Dic):
    print(key,Dic[key])
print("desc")
for key in reversed(sorted(Dic)):
    print(key,Dic[key])