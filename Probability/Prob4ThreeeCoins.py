x=int(input('Enter number of coins to be tossed'))
face=['H']*x
coinface=['H']*x
face2=['T']*x
coinface2=['T']*x
permutation=[]
permutation2=[]
finalpermutation=[]

for i in range(0,3):
    coinface[i]="T"
    permutation.append("".join(coinface))
    coinface = ['H'] * x
permutation.append("".join(face))

for i in range(0,3):
    coinface2[i]="H"
    permutation2.append("".join(coinface2))
    coinface2 = ['T'] * x
permutation2.append("".join(face2))


finalpermutation=permutation+permutation2
print(finalpermutation)

count=0
for i in finalpermutation:
    if i in'HHH':
        count=count+1
print(count)
print("Probability of:",count/len(finalpermutation))
count=0
for i in finalpermutation:
    if i in'TT':
        print(i)
        count=count+1
print(count)
print("Probability of:",count/len(finalpermutation))
