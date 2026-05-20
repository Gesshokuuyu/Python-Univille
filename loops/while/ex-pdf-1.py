# Crie um programa no qual o usuário informe a idade de um número indeterminado de
# alunos. Para encerrar a leitura dos dados, o usuário deve informar uma idade negativa.
# No final, o programa deve mostrar a média aritmética entre a maior e a menor idade

idadeI = 0
menorI = 0
maiorI = 0

while (idadeI >= 0):
    idadeI = int(input("Informe uma idade: "))

    if(idadeI > 0 and idadeI > maiorI):
        maiorI = idadeI

    if(menorI == 0):
        menorI = idadeI

    elif(idadeI > 0 and idadeI < menorI):
        menorI = idadeI



print(f"A menor idade informada é {menorI}")
print(f"A maior idade informada é {maiorI}")

media = (maiorI + menorI) / 2
print(f"A média é {media}")