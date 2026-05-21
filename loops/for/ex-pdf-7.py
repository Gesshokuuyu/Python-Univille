# Os números primos possuem várias aplicações dentro da Ciência de Dados em
# criptografia e segurança, por exemplo. Um número primo é aquele que é divisível
# apenas por um e por ele mesmo. Assim, faça um programa que peça um número
# inteiro e determine se ele é ou não um número primo

numero = int(input("Informe um numero: "))

if(numero % 2 != 0):
    print("Numero impar")
else:
    print("Numero primo")