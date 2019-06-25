y = [[12,7,3],[4 ,5,6],[7 ,8,9]]
print(y)
z = [[0,0,0],[0,0,0],[0,0,0]]
mul=9
print('multiplied by',mul)
for i in range(len(y)):
    for count in range(len(y[0])):
        z[i][count] = 9*y[i][count]
print(z)