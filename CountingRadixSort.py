def countingSort(lista, k):
    
    #tamanho do array
    n = len(lista)
    #elemento maior
    m = max(lista)+1 
    #Contador
    count = [0]*m 
    #array de saída
    saida = [0]*n
    
    #Conta as ocorrências dos elementos
    for i in lista:
        count[(i/k)%10] += 1             
    
    #count contém os elementos menores ou iguais a i
    for i in range(1, m):            
        count[i] += count[i-1]
        
    #enche a lista de saída com os números ordenados de forma crescente
    for i in reversed(range(0, n)):
        saida[count[ (lista[i]/k) %10]-1] = lista[i]
        count[(lista[i]/k)%10] -=1
            
    return (saida)


def radixSort(lista): 
   
    m1 = max(lista) 
  
    k = 1
    
    while m1/k > 0: 
        lista = countingSort(lista,k) 
        k *= 10
    
    return(lista)


lista = [10, 4, 700, 2, 1, 3, 2, 1, 4, 2, 3, 2, 1]        
radixSort(lista) 
  
print(lista)