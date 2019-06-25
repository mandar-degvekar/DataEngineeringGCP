x=int(input("Enter Value for n:"))
if(x!=0):
    dic={1:1}
    for i in range(1,x+1):
        dic[i]=i*i

else:
    print("cant create dictionary since n=",x)
print(dic)