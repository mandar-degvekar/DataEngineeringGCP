def replacment(s):
    print(s)
    if(len(s)<=3):
        print('NA lenghth is less than 3',s)
    elif s[-3:] == 'ing':
        s=s[0:len(s)-3]+'ly'
    else:
        s=s+'ing'
    return s
inm=input('Enter string')
print(replacment(inm))





