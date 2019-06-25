X = [[ 5, 1 ,3], [ 1, 1 ,1], [ 1, 2 ,1]]
Y = [[1], [2], [3]]
z = [0,0,0]
for i in Y:
    for j in range(len(X[0])):
       print(i*X[j][0])
