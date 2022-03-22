#find factorial using recursion

def fact(i):
    if i<=1:
        return i;
    else:
        return (i*fact(i-1))

n = int(input('enter the number: '))
if n<1:
    print('enter positive non zero number')
elif n==0:
    x = 1;
else:
    x = fact(n)
print('fact is',x)
