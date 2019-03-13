def quickSort(lista, inicio, fim):
    if inicio < fim:
        pivo = partition(lista, inicio, fim)
        quickSort(lista, inicio, pivo-1)
        quickSort(lista, pivo+1, fim)


def partition(lista, primeiro, ultimo):
    pivo = lista[primeiro]
    esquerda = primeiro + 1
    direita = ultimo
    done = False

    while not done:
        while esquerda <= direita and lista[esquerda] <= pivo:
            esquerda = esquerda + 1
        
        while lista[direita] >= pivo and direita >= esquerda:
            direita = direita - 1
        
        if direita < esquerda:
            done = True
        else:
            temporario = lista[esquerda]
            lista[esquerda] = lista[direita]
            lista[direita] = temporario
    
    temp = lista[primeiro]
    lista[primeiro] = lista[direita]
    lista[direita] = temp

    return direita






