# Com base na tabela salarial da questão anterior, crie um pro grama que informe a
# quantidade de médicos com salários superiores a R$ 4.500,00.


salarioEnf = 0
salarioNut = 0
salarioMed = 0

salCorte = float(4500)

qtdMedicosMaior = 0
contador = 0

while(True):
    codigo = int(input('Informe o código de cargo(0 para sair):'))
    if(codigo == 1):
        print("Cargo: Enfermeiro")
        print("=================")
        salarioEnf = float(input("Salario: "))
    elif(codigo == 2):
        print("Cargo: Nutricionista")
        print("=================")
        salarioNut = float(input("Salario: "))
    elif(codigo == 3):
        print("Cargo: Médico")
        print("=================")
        salarioMed = float(input("Salario: "))
        if(salarioMed > salCorte):
            contador += 1
    elif(codigo == 0): 
        break
    else:
        print("cargo inválido, digite novamente")


if(contador > 0):
    print(f"A quantidade de médicos com salários maiores que R$4.500 é {contador}")
