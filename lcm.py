#Python Program to Find LCM using function
#lcm*hcf = n1*n2
def hcf(x,y):
    if x>y: smaller = y;
    else: smaller = x;
    for i in range(1,smaller+1):
        if x%i==0 and y%i ==0:
            h = i
    return h

def lcm(x,y):
    l = x*y//hcf(x,y)
    return l

n1 = int(input('enter number n1: '))
n2 = int(input('enter number n2: '))
res = lcm(n1,n2)
res2 = hcf(n1,n2)
print('The lcm of 2 numbers is {}'.format(res))
