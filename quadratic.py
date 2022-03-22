'''program to find the solution of the quadratic equation'''
import math as m
a = float(input('enter coefficent a'))
b= float(input('enter coefficient b'))
c = float(input('enter coefficent c'))
d = (b**2) - (4*a*c)
x1 = (-b+m.sqrt(d))/(2*a)
x2 = (-b-m.sqrt(d))/(2*a)
print('The solution of the quadratic equation are {}, {}'.format(x1,x2))
