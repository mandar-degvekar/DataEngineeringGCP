duplist=[1,2,3,2,3,4,5,6,5]
finallist=[]
for i in duplist:
    if i not in finallist:
        finallist.append(i)
print(finallist)