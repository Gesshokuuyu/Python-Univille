# 16 - Considere que o último concurso vestibular apresentou três provas: Português, Matemática
# e Conhecimentos Gerais. Considerando que para cada candidato tem-se um registro contendo
# o seu nome e as notas obtidas em cada uma das provas, construa um algoritmo que forneça:
# a) o nome e as notas em cada prova do candidato
# b) a média do candidato
# c) uma informação dizendo se o candidato foi aprovado ou não
# Considere que um candidato é aprovado se sua média for maior que 7.0 e se não apresentou
# nenhuma nota abaixo de 5.0

candidato = input('Informe o nome do candidato: ')

portugues = float(input('Informe a nota em portugues: '))
matematica = float(input('Informe a nota em matematica: '))
conhecimentos = float(input('Informe a nota em Conhecimentos Gerais: '))

media = (portugues + matematica + conhecimentos) / 3
menorNota = min(portugues, matematica, conhecimentos)

if media >= 7 and menorNota >= 5:
    print(f'O candidato: {candidato} foi aprovado com a média maior que 7 e todas as notas maiores que 5. \n Média final: {media}')
elif media >= 7 and menorNota < 5:
    print(f'O candidato: {candidato} foi aprovado com a média maior que 7 e com uma nota menor que 5. \n Média final: {media}')
else: 
    print(f'O candidato: {candidato} foi reprovado com a média {media}')