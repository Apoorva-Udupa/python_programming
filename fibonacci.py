#Python Program to Print the Fibonacci sequence
num = int(input('enter number: '))
a = 0; b = 1
count = 0
while count<num:
    print(a)
    nth = a+b
    a = b
    b = nth
    count = count+1
