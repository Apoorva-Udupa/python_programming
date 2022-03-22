#convert decimal to binary

def conv(n):
    if n>1:
        (conv(n//2))
    print(n%2, end='')

dec = int(input('enter non fractional number: '))
if dec<0:
    print('enter positive integer')
else:
    conv(dec)
