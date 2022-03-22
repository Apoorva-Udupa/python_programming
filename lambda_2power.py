#Python Program to Display Powers of 2 Using Anonymous Function
#anonymous function is lambda function
num = int(input('enter number of terms u need to find the power of: '))
result = list(map(lambda x: 2**x, range(num)))
for i in range(num):
    print('2 raise to power {} is {}'.format(i,result[i]))
