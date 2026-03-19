# O sistema de avaliação de determinada disciplina, é composto por três provas. A primeira
# prova tem peso 2, a segunda tem peso 3 e a terceira tem peso 5. Faça um algoritmo para calcular
# a média final de um aluno desta disciplina.
pp1 = 2 
pp2 = 3
pp3 = 5

nome = input('Informe o nome do aluno: ')

nota1 = float(input('Informe a nota da primeira prova: '))
nota2 = float(input('Informe a nota da segunda prova: '))
nota3 = float(input('Informe a nota da terceira prova: '))

media = ((nota1 * pp1) + (nota2 * pp2) + (nota3 * pp3)) / (pp1 + pp2 + pp3)

print(f'A média final de {nome} é {media:.2f}')

