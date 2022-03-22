#python program to find factors of a number 
def factors(x):
    print('The factors of {} are: '.format(x))
    for i in range(1,x+1):
        if x%i==0:
            print(i,end = '\t')
n = int(input('enter the numbers to find the factors: '))
factors(n)
