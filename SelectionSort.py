def selectionSort(list):
    for i in range(len(list)):
        minPosition = i

        for j in range(i+1, len(list)):
            if list[minPosition] > list[j]:
                minPosition = j
        
        templist = list[i]
        list[i] = list[minPosition]
        list[minPosition] = templist
    
    return list

print(selectionSort([5,2,1,9,0,4,6]))