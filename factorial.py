#python program to find the factorial of a number 
num = int(input('enter the number: '))
fact = 1
for i in range(1,num+1):
    fact = fact*i
print(fact)
