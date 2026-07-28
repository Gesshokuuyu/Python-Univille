import math

print('--------------------Area do Cilindro--------------------')

altura = float(input('Informe a altura(M): '))
raio = float(input('Informe o raio do Cilindro(M): '))

areaB = 3.14 * raio ** 2
areaL = 2 * 3.14 * raio * altura

areaT = areaB * 2 + areaL

litragem = areaT / 3
latasN = math.ceil(litragem / 5)
preco =float(latasN * 20)
print('\n')
print(f'A Litragem necessária é de {litragem:.2f}, \n a quantidade de latas a comprar {int(latasN)} \n e o preço final saí por R$ {preco:.2f}')

