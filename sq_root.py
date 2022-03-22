'''In this program, you'll learn to find the square root of a number using exponent operator and cmath module.'''
#for float numbers
import math as m
p = float(input('enter the number to find its square root'))
s = m.sqrt(p)
print(s)
#for complex number 
import cmath as c
k = eval(input('enter the complex number to find its square root'))
l = cmath.sqrt(k)
print("the square root of given complex number is {0:0.3f}+{1:0.3f}".format(l.real,l.imag))
