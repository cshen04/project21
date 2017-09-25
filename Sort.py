import time
import random

def selection_sort(arr):
    for k in range(0,len(arr)):
        minimum = arr[k]
        exchange = k
        i = k
        while i < len(arr):
            if arr[i] < minimum:
                minimum = arr[i]
                exchange = i
            i = i + 1
        arr[exchange] = arr[k]
        arr[k] = minimum
    return arr

def insertion_sort(arr):
      for k in range(1, len(arr)):
        cur = arr[k]
        j = k
        while j > 0 and arr[j-1] > cur:
            arr[j] = arr[j-1]
            j = j - 1
        arr[j] = cur

if __name__ == '__main__':
    List1000 = [None] * 1000
    List1002 = [None] * 1000
    List1003 = [None] * 1000
    List1 = [None] * 1000
    Lista = [None] * 1000
    ListI = [None] * 1000
    List2500 = [None] * 2500
    List2502 = [None] * 2500
    List2503 = [None] * 2500
    List2 = [None] * 2500
    Listb = [None] * 2500
    ListII = [None] * 2500
    List5000 = [None] * 5000
    List5002 = [None] * 5000
    List5003 = [None] * 5000
    List3 = [None] * 5000
    Listc = [None] * 5000
    ListIII = [None] * 5000
    List7500 = [None] * 7500
    List7502 = [None] * 7500
    List7503 = [None] * 7500
    List4 = [None] * 7500
    Listd = [None] * 7500
    ListIV = [None] * 7500
    List10000 = [None]* 10000
    List10002 = [None]* 10000
    List10003 = [None]* 10000
    List5 = [None]* 10000
    Liste = [None]* 10000
    ListV = [None]* 10000
    incrArr = [List1000, List2500, List5000, List7500, List10000]
    decrArr = [List1002, List2502, List5002, List7502, List10002]
    randArr = [List1003, List2503, List5003, List7503, List10003]
    i1 = [List1, List2, List3, List4, List5]
    i2 = [Lista, Listb, Listc, Listd, Liste]
    i3 = [ListI, ListII, ListIII, ListIV, ListV]

    for i in range(0, len(randArr)):
        increment = 0
        while increment < len(randArr[i]):
            randArr[i][increment] = random.randint(0,10000)
            i3[i][increment] = randArr[i][increment]
            increment += 1

    for i in range(0,len(incrArr)):
        count = 0
        for index in range(0,len(incrArr[i])):
            incrArr[i][index] = count
            i1[i][index] = count
            count += 1


    for i in range(0,len(decrArr)):
        count = len(decrArr[i])-1
        for index in range(0,len(decrArr[i])):
            decrArr[i][index] = count
            i2[i][index] = count           
            count -= 1 

    totalArr  = [incrArr, decrArr, randArr]
    totalArr2 = [i1,i2,i3] 
    timeList  = []
    timeList2 = []

    for i in totalArr:
        for List in i:
            start = time.clock()
            insertion_sort(List)
            end = time.clock()
            timeList.append(end-start)

    for i in totalArr2:
        for List in i:
            start = time.clock()
            selection_sort(List)
            end = time.clock()
            timeList2.append(end-start)    
    print('1000 Increasing Insertion: ' + '{:.20f}'.format(timeList[0]))
    print('2500 Increasing Insertion: ' + '{:.20f}'.format(timeList[1]))
    print('5000 Increasing Insertion: ' + '{:.20f}'.format(timeList[2]))
    print('7500 Increasing Insertion: ' + '{:.20f}'.format(timeList[3]))
    print('10000 Increasing Insertion: ' + '{:.20f}'.format(timeList[4]))
    print('1000 Decreasing Insertion: ' + '{:.20f}'.format(timeList[5]))
    print('2500 Decreasing Insertion: ' + '{:.20f}'.format(timeList[6]))
    print('5000 Decreasing Insertion: ' + '{:.20f}'.format(timeList[7]))
    print('7500 Decreasing Insertion: ' + '{:.20f}'.format(timeList[8]))
    print('10000 Decreasing Insertion: ' + '{:.20f}'.format(timeList[9]))
    print('1000 Random Insertion: ' + '{:.20f}'.format(timeList[10]))
    print('2500 Random Insertion: ' + '{:.20f}'.format(timeList[11]))
    print('5000 Random Insertion: ' + '{:.20f}'.format(timeList[12]))
    print('7500 Random Insertion: ' + '{:.20f}'.format(timeList[13]))
    print('10000 Random Insertion: ' + '{:.20f}'.format(timeList[14]))
    print('1000 Increasing Selection: ' + '{:.20f}'.format(timeList2[0]))
    print('2500 Increasing Selection: ' + '{:.20f}'.format(timeList2[1]))
    print('5000 Increasing Selection: ' + '{:.20f}'.format(timeList2[2]))
    print('7500 Increasing Selection: ' + '{:.20f}'.format(timeList2[3]))
    print('10000 Increasing Selection: ' + '{:.20f}'.format(timeList2[4]))
    print('1000 Decreasing Selection: ' + '{:.20f}'.format(timeList2[5]))
    print('2500 Decreasing Selection: ' + '{:.20f}'.format(timeList2[6]))
    print('5000 Decreasing Selection: ' + '{:.20f}'.format(timeList2[7]))
    print('7500 Decreasing Selection: ' + '{:.20f}'.format(timeList2[8]))
    print('10000 Decreasing Selection: ' + '{:.20f}'.format(timeList2[9]))
    print('1000 Random Selection: ' + '{:.20f}'.format(timeList2[10]))
    print('2500 Random Selection: ' + '{:.20f}'.format(timeList2[11]))
    print('5000 Random Selection: ' + '{:.20f}'.format(timeList2[12]))
    print('7500 Random Selection: ' + '{:.20f}'.format(timeList2[13]))
    print('10000 Random Selection: ' + '{:.20f}'.format(timeList2[14]))