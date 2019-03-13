def mergeSort(lista):
    if len(lista)>1:
        metade = len(lista)//2
        parte1 = lista[:metade]
        parte2 = lista[metade:] 

        mergeSort(parte1)
        mergeSort(parte2)

        i = 0
        j = 0
        k = 0

        while i < len(parte1) and j < len(parte2):
            if parte1[i] < parte2[j]:
                lista[k] = parte1[i]
                i = i+1
            else:
                lista[k] = parte2[j]
                j = j+1
            k = k+1
        
        while i < len(parte1):
            lista[k] = parte1[i]
            i = i+1
            k = k+1

        while j < len(parte2):
            lista[k] = parte2[j]
            j = j+1
            k = k+1

    print(lista)

