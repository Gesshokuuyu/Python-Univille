print("Análise de preços:")

p1 = float(input("Informe o preço do 1° produto: "))
p2 = float(input("Informe o preço do 2° produto: "))
p3 = float(input("Informe o preço do 3° produto: "))

if(p1 > p2):
    if(p2 > p3):
        print("Voce deve comprar o terceiro produto")
    elif(p2 == p3 ):
        print("Escolha entre o produto 2 e 3.")
    else:
        print("Compre o segundo produto")
else: 
    if(p1 > p3):
        print("compre o terceiro produto.")
    elif(p1 == p3 ):
        print("Escolha entre o produto 1 e 3.")
    else:
        print("COmpre o primeiro prdouto")