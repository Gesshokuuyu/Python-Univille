# Crie um programa no qual o usuário informe o código do cargo de um funcionário (ver
# tabela abaixo) e o seu respectivo salário. Para encerrar a leitura dos dados, defina uma
# condição de parada (por exemplo, código do cargo igual a zero). Ao fim, o programa deve
# informar a média salarial dos nutricionistas.

#  cod      |      nome
#   1       |    Enfermeiro
#   2       |   Nutricionista
#   3       |     Médico


salarioEnf = 0
salarioNut = 0
salarioMed = 0

salarioTotalNut = 0
contador = 0

while(True):
    codigo = int(input('Informe o código de cargo(0 para sair):'))
    if(codigo == 1):
        print("Cargo: Enfermeiro")
        print("=================")
        salarioEnf = float(input("Salario: "))
    elif(codigo == 2):
        contador += 1
        print("Cargo: Nutricionista")
        print("=================")
        salarioNut = float(input("Salario: "))
        salarioTotalNut += salarioNut
    elif(codigo == 3):
        print("Cargo: Médico")
        print("=================")
        salarioMed = float(input("Salario: "))
    else: 
        print("cargo inválido, digite novamente")

    if(codigo == 0):
        break


if(contador > 0):
    media = salarioTotalNut / contador
    print(f"A média salarial dos nutricionistas é {media}")
