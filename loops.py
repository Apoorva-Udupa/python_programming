'''Task
The provided code stub reads and integer n, from STDIN. For all non-negative integers i<n, print i^2.'''
if __name__ == '__main__':
  n = int(input(''))
  if n>=1 and n<=20:
    i = 0;
    while(i<n):
      print(i**2)
      i = i+1
