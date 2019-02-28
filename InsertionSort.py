def insertionSort(list):
    for i in range(1, len(list)):
        current = list[i]

        while i > 0 and list[i - 1] > current:
            list[i] = list[i - 1]
            i = i - 1
            list[i] = current

    return list


print(insertionSort([5, 2, 1, 9, 0, 4, 6]))
