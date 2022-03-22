#find sum of first n natural numbers using recursion
def sum(i):
    if i<=1:
        return i;
    else:
        return (i+sum(i-1))

n = int(input('enter the number: '))
if n<0:
    print('enter a positive number')
else:
    print('sum is',sum(n))
