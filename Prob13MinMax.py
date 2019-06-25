from Utility import  util as u
x=input("enter comma seprated values to be iserted in the list:")
list=x.split(',')
li=u.splitandlist(list)
print(li)
li.sort()
print(li)
print("using sort smallest number is ",li[0])
print("using sort largest number is",li[-1])

max=li[0]
min=li[0]
for i in li:
    if(max<i):
        max=i
    elif(min>i):
        min=i

print("using loop largest", max)
print("using loop smallest", min)
