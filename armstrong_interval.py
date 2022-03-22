#Python Program to find Armstrong Number in internal
r1 = int(input('enter lower number in range:'))
r2 = int(input('enter highest number in range:'))
for num in range(r1,r2+1):
    cop = num
    sum = 0
    while num > 0:
        d = num%10
        sum = sum+(d**3)
        num //= 10
    if cop == sum:
        print(cop)
