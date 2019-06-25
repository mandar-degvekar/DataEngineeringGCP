import array
sar=array.array('i',[1,1,2,3,4,5,2,8,5,8])
#sar=sorted(arr)
print(sar)
x=int(input('Enter number to be removed'))
try:
    sar.remove(x)
except:
    print("number",x,"is not avaialable in list please enter valid number")
print(sar)