# Construir um programa que efetue o cálculo do salário líquido de um funcionário. Para
# fazer este programa, você deve possuir alguns dados, tais como: valor da hora, número de horas
# trabalhadas no mês e percentual de desconto do INSS. Em primeiro lugar, deve-se estabelecer
# qual será o seu salário bruto para efetuar o desconto e ter o valor do salário líquido.

valorHora       = float(input('Informe o valor por hora trabalhada: '))
cargaHoraria    = int(input('Informe o valor de horas trabalhadas: '))
percentualINSS  = float(input('Informe a porcentagem de desconto do INSS: '))

salarioBruto = valorHora * cargaHoraria
salarioLiquido = salarioBruto * (1 - (percentualINSS /100))

print(f'O salario bruto deverá ser: {salarioBruto}')

print(f'O salario liquido deverá ser: {salarioLiquido}')