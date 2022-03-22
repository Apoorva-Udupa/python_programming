'''Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.'''
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list1 = list(arr)
    max1 = max(list1)
    list2 = list()
    #print(max1)
    for i in list1:
      if max1>i:
        list2.append(i)
    #print(list2)
    max2 = max(list2)
    print(max2)
