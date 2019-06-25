import array
arr=array.array('i',[1,2,3,4,5])
print('created array is')
for i in range(0,5):
    print(arr[i])
c = []
print('reversed array is')
for i in reversed(range(0,5)):
    c.append(arr[i])
brr=array.array('i',c)
print(brr)
