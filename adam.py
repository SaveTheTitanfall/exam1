import numpy as np
a = np.array([[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0]])
b = np.copy(a)

for i in range(len(a)):
    a[i, i] = (1+i)**2

for i in range(4):
    b[i, i+3] = i+1

c = np.array([[0, 0, 0, 0, 0, 0, 0],[
    4, 0, 0, 0, 0, 0, 0],
    [0, 6, 6, 0, 0, 0, 0],
    [0, 0, 8, 8, 0, 0, 0],
    [0, 0, 0, 10, 0, 0, 0],
    [0, 0, 0, 0, 12, 0, 0],[0, 0, 0, 0, 0, 14, 0]])

mainMatrix = a + b + c
for i in range(6):
    mainMatrix[4, i+1] += 2

Transmat = np.transpose(mainMatrix)
asgf= mainMatrix * Transmat
