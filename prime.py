#Python Program to Check Prime Number
flag = False
num = int(input('enter the number: '))
if num>1:
    for i in range(2,num):
        if num%i == 0:
            flag = True
            break

if flag == False: print("{} is prime".format(num))
elif flag == True: print('{} is not prime'.format(num))
