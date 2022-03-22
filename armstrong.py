#Python Program to Check Armstrong Number
num = int(input('enter number to check if it is an armstrong number:'))
cop = num
sum =0
while num>0:
    d = num%10
    sum = sum+(d**3)
    num = int(num//10)
if cop == sum:
    print('armstrong number')
else:
    print('not armstrong number')
