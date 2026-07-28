#  Escreva um programa que peça dois números inteiros e imprima todos os
# números inteiros entre eles.

inicio = int(input("Informe o °1 numero: "))
fim = int(input("Informe o °2 numero: "))
step = 1

print(f"entre i1({inicio}) até i2({fim}): ")

if inicio > fim:
    step = -1
    inicio -= 1
else:
    inicio += 1

for i in range(inicio, fim, step):
    print(i)
