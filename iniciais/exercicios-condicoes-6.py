#  Faça um algoritmo que leia dois números A e B e mostre o maior deles.

a = int(input('Informe um numero: '))
b = int(input('Informe outro numero: '))

maior = max(a, b)

if a == b:
    print('Os numeros são iguais')
else:
    print(f'O maior numero entre {a} e {b} é {maior}')
