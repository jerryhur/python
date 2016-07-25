def selectionSort(unSortedList):    

    for i in range(len(unSortedList)):        
        index = i
        minNumber = unSortedList[i]
        for j in range(i+1, len(unSortedList)):
            if minNumber > unSortedList[j]:
                index = j
                minNumber = unSortedList[j]
        tempNumber = unSortedList[i]
        unSortedList[i] = unSortedList[index]
        unSortedList[index] = tempNumber
        
    return unSortedList

print(selectionSort([11, 1, 5, 3, 2]))
