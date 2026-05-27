# Os números primos possuem várias aplicações dentro da Ciência de Dados em
# criptografia e segurança, por exemplo. Um número primo é aquele que é divisível
# apenas por um e por ele mesmo. Assim, faça um programa que peça um número
# inteiro e determine se ele é ou não um número primo

numero = int(input("Informe um número: "))

qtdDivisores = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        qtdDivisores += 1


if(qtdDivisores > 2):
    print("Numero não é primo")
else:
    print("Numero 1é primo")
