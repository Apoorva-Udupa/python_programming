#python program to find hcf or gcd of 2 numbers
def hcf(a,b):
    if a>b: small = b;
    else: small = a;
    for i in range(1,small+1):
        if a%i==0 and b%i==0:
            hcf = i
    return hcf
a = int(input('enter a: '))
b = int(input('enter b: '))
h = hcf(a,b)
print('The hcf of {} and {} is {}'.format(a,b,h))
