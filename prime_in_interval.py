#Python Program to print all prime numbers in the interval
l_range = int(input('enter lower range number: '))
u_range = int(input('enter upper range number: '))

for num in range(l_range, u_range + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
