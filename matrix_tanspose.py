#program to find the tanspose of a matrix
x = [[2,3],[4,5],[6,7]]
result = [[x[j][i] for j in range(len(x))]for i in range(len(x[0]))]
for i in result:
    print(i)

#or
result2 = [[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        result2[j][i] = x[i][j];
for i in result2:
    print(i)
