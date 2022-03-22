'''Given the names and grades for each student in a class of n students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.'''
if __name__ == '__main__':
    list1 = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list1.append([name,score])
    #print(list1)
    list2 = list()
    for i in range(0,len(list1)):
        list2.append(list1[i][1])
    list2.sort()
    #print(list2)
    list2 = list(dict.fromkeys(list2))
    a = list2[1]
    #print(a)
    list3 = list()
    for i in range(0,len(list1)):
      if list1[i][1]==a:
        list3.append(list1[i][0])
    list3.sort()
    for x  in list3:
      print(x)
