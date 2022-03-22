'''Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.

str.isalnum()
This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
str.isalpha()
This method checks if all the characters of a string are alphabetical (a-z and A-Z).
str.isdigit()
This method checks if all the characters of a string are digits (0-9).
str.islower()
This method checks if all the characters of a string are lowercase characters (a-z).
str.isupper()
This method checks if all the characters of a string are uppercase characters (A-Z).
Task

You are given a string .
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.'''
if __name__ == '__main__':
    s = input()
    for i in s:
        if i.isalnum():
            print('True')
            break
    else:
        print('False')
    for i in s:
        if i.isalpha():
            print('True')
            break
    else:
        print('False')
    for i in s:
        if i.isdigit():
            print('True')
            break
    else:
        print('False')
    for i in s:
        if i.islower():
            print('True')
            break
    else:
        print('False')
    for i in s:
        if i.isupper():
            print('True')
            break
    else:
        print('False')
            
