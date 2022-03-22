#python program to print multiplication table of the given number
num = int(input('enter the number for nultiplication table: '))
for i in range(1,11):
    print('{} * {} = {}'.format(num,i,num*i))
    
