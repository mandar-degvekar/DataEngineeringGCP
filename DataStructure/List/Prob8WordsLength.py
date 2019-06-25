l=['mandar','naruto','kiba','kisame','guy','itachi','orochimaru','tsunade','jiraiya']
finallist=[]
sel=int(input('Enter length for word selection:'))
for i in l:
    if(len(i)>sel):
        finallist.append(i)
print(finallist)
