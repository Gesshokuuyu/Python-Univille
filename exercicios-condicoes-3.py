# Faça um programa para aprovar empréstimos bancários. O código deve pedir três
# informações: valor do empréstimo, número de parcelas e salário do solicitante. Aprovar
# empréstimo caso o valor das parcelas represente no máximo 30% do salário do solicitante.

print('\n______________________BRADESCO______________________')
print('\n-------------------------------------------------------')
print('\n______________________Empréstimos______________________')

valorEmprestimo = float(input("Iforme o valor desejado para empréstimo"))
qtdParcelas = int(input('Informe em quantas parcelas será pago: '))
salarioSolicitante = float(input('Informe o salário do solicitante'))

print('\n_____________Processando_____________\n')
valorPorParcela = valorEmprestimo / qtdParcelas
porcentagemSalarial = valorPorParcela / salarioSolicitante * 100

if porcentagemSalarial <= 30: 
    print(f'O empréstimo solicitado de {salarioSolicitante:.2f} dividido em {qtdParcelas} parcelas foi aprovado!')
else:
    print(f'O valor do empréstimo foi negado por não bater o valor de parcela ao comparar com o salário, \n sendo como requisito minimo 30% do salario por parcela\n o seu empréstimo bate em {porcentagemSalarial}%')