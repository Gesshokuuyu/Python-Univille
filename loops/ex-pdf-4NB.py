# Faça um algoritmo que leia informações de alunos (Matricula, Nota1, Nota2 , Nota3)
# com o fim das informações indicado por Matricula = 9999. Para cada aluno deve ser
# calculada a média final de acordo com a seguinte fórmula:

#  Média final = [(2 * Nota1) +(3* Nota2) +(4* Nota 3)] / 9
# Se a média final for igual ou superior a 5, o algoritmo deve mostrar Matrícula, Média
# Final e a mensagem "APROVADO".

# Se a média final for inferior a 5, o algoritmo deve mostrar Matricula, Média Final e a
# mensagem "REPROVADO".
# Ao final devem ser mostrados o total de aprovados, o total de alunos da turma e o total
# de reprovados.
# Agora sem usar while true, e sem break;

matricula = None
nt1 = 0
nt2 = 0
nt3 = 0
 
totalAp = 0
totalRp = 0
total = 0
media = 0

while matricula != 9999:
    matricula = int(input("Informe a Matricula do aluno: "))
    if matricula != 9999:

        total += 1

        nt1 = float(input("Informe a nota 1: "))
        nt2 = float(input("Informe a nota 2: "))
        nt3 = float(input("Informe a nota 3: "))
        media = ((2 * nt1) +(3 * nt2) + (4 * nt3)) / 9

        if(media < 5):
            situacao = "Reprovado"
            totalRp += 1
        else:
            situacao = "Aprovado"
            totalAp += 1

        print("")
        print("")
        print("|========== Ficha Escolar ==============")
        print(f"| Matricula: {matricula}            ")
        print("|=======================================")
        print(f"| Média: {media:.2f}                ")
        print(f"| Situação: {situacao}              ")
        print("|=======================================")
        print("")
        print("")

print("")
print("====================================================================")
print(f"Total de alunos processados: {total}")
print(f"Total de alunos aprovados: {totalAp}")
print(f"Total de alunos reprovados: {totalRp}")
print("====================================================================")
    