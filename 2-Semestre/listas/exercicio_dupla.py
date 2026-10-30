lista = [1, 8, 6, 2, 1]
for key, value in enumerate(lista):
    minKey = key

    for i in range(key + 1, len(lista)):
        if lista[i] <= lista[minKey]:
            minKey = i

    lista[key], lista[minKey] = lista[minKey], lista[key]

    print(lista, "ROTAÇÃO:", key)
            

