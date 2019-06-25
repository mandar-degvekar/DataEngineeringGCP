def replacment(s):
    print(s)

    sliceds = s[1:len(s)]
    inp = input('Enter char to be replaced in given string')
    print('after $ replacement')
    for i in range(2, len(sliceds) - 1):
        if inp == sliceds[i]:
            sliceds = sliceds.replace(sliceds[i], '$')
            break

    s = s[0] + sliceds
    return s


a=input('Enter string')
print(replacment(a))
