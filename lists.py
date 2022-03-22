'''Task: Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at i position.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.'''
if __name__ == '__main__':
    N = int(input())
    list1 = list()
    values = list()
    for i in range(N):
      values.append(input())
    val = []
    for i in values:
      a = i.split(' ')
      val.append(a)
    #create blank list
    blank = list()
    #extract commands
    for i in range(0,len(val)):
      if val[i][0]=='insert':
       blank.insert(int(val[i][1]),int(val[i][2])) 
      elif val[i][0]=='print':
        print(blank)
      elif val[i][0]=='remove':
        blank.remove(int(val[i][1]))
      elif val[i][0]=='append':
        blank.append(int(val[i][1]))
      elif val[i][0]=='sort':
        blank.sort()
      elif val[i][0]=='pop':
        blank.pop()
      elif val[i][0]=='reverse':
        blank.reverse()
