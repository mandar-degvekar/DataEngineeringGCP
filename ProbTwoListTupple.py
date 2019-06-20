def splitandlist(input):
    l=[]
    for i in input:
        try:
            int(i)
            l.append(i)

        except:
            print(i + " is not a number")


    return l

inputList=input("enter numeric values use comma for separation:")
list=inputList.split(',')
list2=splitandlist(list)
print("list val=",list2)
print("tupple value=",tuple(list2))


