import numpy as np

l=[0,1,2,3,4,5,6,7,8]
count=0
fstr=''
for i in l:
    if(count<3):
        fstr=fstr+' '+str(i)
        count=count+1
    else:
        fstr=fstr+';'
        fstr = fstr + ' ' + str(i)
        count=1
print(fstr)
a=np.matrix(fstr)
print(a)