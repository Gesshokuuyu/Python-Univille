# 4) Colete novamente 5 inteiros e imprima a lista em ordem inversa à enviada.

lista = list()

for i in range(5):
    lista.append(int(input(f"Insira um numero para a posição {i} da lista: ")))

for i in range(len(lista) - 1, -1, -1):
    print(i)