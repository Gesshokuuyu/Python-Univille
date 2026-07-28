#  Desenvolva um programa que leia um conjunto indeterminado de temperaturas
# em Celsius e informe a média delas. A leitura deve ser encerrada ao ser enviado o
# valor -273°C.

temp = float(input("Informe uma temperatura em °C: "))
soma = 0
c = 0

while temp != -273:
    soma += temp
    c +=1    
    temp = float(input("Informe uma temperatura em °C (para encerrar digite -273): "))

if c > 1:
    media = soma / c
    print(f"A media entre as temperaturas informadas é de {media}")
else:
    print("Programa encerrado sem uma Temperatura informada anteriormente")