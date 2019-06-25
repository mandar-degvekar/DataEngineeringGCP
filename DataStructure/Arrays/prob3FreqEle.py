import array
arr=array.array('i',[1,1,2,3,4,5,2,8,5])
count=0
x=int(input('Enter number to be searched'))
sar=sorted(arr)

for i in range(0,len(sar)):
        if(x==sar[i]):
            count=count+1
print("for element",x,"Frequency is",count)



