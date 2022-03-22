#add 2 matrices 
x = [[1,2,3],[4,5,6],[7,8,9]]
y = [[10,10,11],[2,3,4],[6,3,6]]
result = [[x[i][j]+y[i][j]  for j in range(len(x[0]))]  for i in range(len(x))]
for i in result:
    print(i)
