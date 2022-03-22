#check is the given string is palindrome or not 
my_str = input('enter the string : ')
my_str  =my_str.casefold() #for caseless comparision
rev_str = reversed(my_str)
if list(my_str)==list(rev_str):
    print("It's a palindrome!")
else:
    print('NOT a palindrome:(')
