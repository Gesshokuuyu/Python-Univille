salarioBase = 1500.00
comisBase = 200.00
comisBaseVendaP = 5
corretor = {
    'nome': input('Insira o nome: '),
    'salBase': salarioBase,
    'qtdVendasImoveis': int(input(f'Quantas vendas foram realizadas ?')),
    'valVendas' :float(input('Informe o Valor total das vendas: '))
}

comisTotalB = corretor['qtdVendasImoveis'] * comisBase
comisTotalP = corretor['valVendas'] * 5 / 100
salarioTotal = corretor['salBase'] + comisTotalB + comisBaseVendaP



print(f'O salario de {corretor['nome']} é {salarioTotal:.2f}')