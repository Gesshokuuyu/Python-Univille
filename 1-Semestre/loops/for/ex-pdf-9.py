colaboradores = 20

candidato_1 = 0
candidato_2 = 0
candidato_3 = 0
candidato_4 = 0

nulos = 0
brancos = 0

votosInvalidos = 0

for i in range(colaboradores):
    print("___Votação Gerencial___")
    print("1 - candidato 1 ")
    print("2 - candidato 2 ")
    print("3 - candidato 3 ")
    print("4 - candidato 4 ")
    print("5 - nulo ")
    print("6 - branco ")
    voto = int(input("Voto: "))

    if voto == 1:
        candidato_1 += 1
    elif voto == 2:
        candidato_2 += 1
    elif voto == 3:
        candidato_3 += 1
    elif voto == 4:
        candidato_4 += 1
    elif voto == 5:
        nulos += 1
    elif voto == 6:
        brancos += 1
    else:
        print("Voto inválido.")
        votosInvalidos += 1


porcentagem_nulos = (nulos / colaboradores) * 100
porcentagem_brancos = (brancos / colaboradores) * 100

print("\nResultado da eleição:")
print(f"Candidato 1: {candidato_1} voto(s)")
print(f"Candidato 2: {candidato_2} voto(s)")
print(f"Candidato 3: {candidato_3} voto(s)")
print(f"Candidato 4: {candidato_4} voto(s)")
print(f"Votos nulos: {nulos}")
print(f"Votos em branco: {brancos}")

print(f"\nPorcentagem de votos nulos: {porcentagem_nulos:.1f}%")
print(f"Porcentagem de votos em branco: {porcentagem_brancos:.1f}%")
print(f"Votos inválidos: {votosInvalidos}")
