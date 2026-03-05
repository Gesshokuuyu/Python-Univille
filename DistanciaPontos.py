import math

print('--------------------Distancia entre Pontos--------------------')

x1 = int(input('Informe a posicao X1: '))
x2 = int(input('Informe a posicao X2: '))

y1 = int(input('Informe a posicao y1: '))
y2 = int(input('Informe a posicao y2: '))

sub1 = (x2 - x1) ** 2
sub2 = (y2 - y1) ** 2

sup3 = sub1 + sub2

distancia = math.sqrt(sup3)

print(f'A Distância entre os pontos informados é {distancia:.2f}')
