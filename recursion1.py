#fibonacci sequence using recursion
def r_fibo(i):
    if i<=1:
        return i
    else:
        return (r_fibo(i-1)+r_fibo(i-2))

nterms  = int(input('enter the number of terms: '))
if nterms<0:
    print('enter positive integer')
else:
    for i in range(nterms):
        print(r_fibo(i))
