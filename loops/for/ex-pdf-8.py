# Vamos entender a distribuição de idades de pensionistas de uma empresa de
# previdência. Escreva um programa que leia as idades de uma quantidade não
# informada de clientes e mostre a distribuição em intervalos de [0-25], [26-50], [51-
# 75] e [76-100]. Encerre a entrada de dados com um número negativo

faixa1 = 0  # 0 a 25
faixa2 = 0  # 26 a 50
faixa3 = 0  # 51 a 75
faixa4 = 0  # 76 a 100

while True:
    idade = int(input("Informe a idade (negativo para encerrar): "))

    if idade < 0:
        break

    if 0 <= idade <= 25:
        faixa1 += 1
    elif 26 <= idade <= 50:
        faixa2 += 1
    elif 51 <= idade <= 75:
        faixa3 += 1
    elif 76 <= idade <= 100:
        faixa4 += 1
    else:
        print("Idade fora do intervalo permitido.")

print("\nDistribuição de idades:")
print(f"[0-25]: {faixa1} pessoa(s)")
print(f"[26-50]: {faixa2} pessoa(s)")
print(f"[51-75]: {faixa3} pessoa(s)")
print(f"[76-100]: {faixa4} pessoa(s)")