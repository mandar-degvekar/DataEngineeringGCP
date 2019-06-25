s=set(['abc','xyz','ss','bb','ss','dd'])
print('existing set')
print(s)
r=input('enter value to be removed')
try:
        s.remove(r)
        print('after removing', r)
        print(s)
except:
        print('value is not present in set')
        print(s)
