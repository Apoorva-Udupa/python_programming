#program on matrix multiplication
x = [[1,2,3],[3,5,7],[6,7,8]]
y = [[3,4,2,1],[1,2,3,4],[8,4,6,0]]
if len(x[0])==len(y):
    result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            result[i][j] += x[i][k]*y[k][j]

for i in  result:
    print(i)
    
