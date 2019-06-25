x = [[12,7,3],[4 ,5,6],[7,8,9]]
y = [[5,8,1],[6,7,3],[4,5,9]]
print(len(x))
z = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)):
    for count in range(len(x[0])):
        z[i][count]=x[i][count]+y[i][count]

print(z)
