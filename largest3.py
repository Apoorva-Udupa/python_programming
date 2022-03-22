#program to find largest of 3 numbers
list1 = list()
while True:
    try:
        num = input('when done type "done" else enter number: ')
        if num == 'done':
            break
        num = int(num)
    except:
        print('invalid number')
    list1.append(num)

largest = max(list1)
print('the largest is {}'.format(largest))
