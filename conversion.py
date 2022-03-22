#Python Program to Convert Decimal to Binary, Octal and Hexadecimal
x = int(input('enter the number for conversion'))
b = bin(x)
h = hex(x)
o = oct(x)
print('Binary conversion',b)
print('Hexadecimal conversion',h)
print('octal conversion',o)
