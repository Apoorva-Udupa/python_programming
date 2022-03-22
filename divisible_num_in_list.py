#Python Program to Find Numbers Divisible by 3, using lambda function
list1 = [3,29, 27, 32, 33, 12, 81, 92]
res = list(filter(lambda x: (x%3==0),list1))
print('the numbers divisible by 3 are:')
for x in res:
    print(x)
