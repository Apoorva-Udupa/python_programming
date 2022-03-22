def calculator(ch,a,b):
    if ch == '+': res = a+b;
    elif ch == '-': res = a-b;
    elif ch == '*': res = a*b;
    elif ch == '/': res = a/b;
    else: res = -1;
    return res

ch = input('enter + ->addition, - ->substraction, * ->multiplication and / ->division: ')
a  = float(input('enter a: '))
b  = float(input('enter b: '))
l = calculator(ch,a,b)
print('The result of calulator is: {}'.format(l))
