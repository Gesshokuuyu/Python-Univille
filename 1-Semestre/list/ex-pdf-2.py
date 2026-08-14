# 2) Com os mesmos dados da questão anterior, defina quantas compras foram realizadas acima
# de 3000 reais e calcule a porcentagem quanto ao total de compras

gastos =  [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

qtdCompras = 0 
qtdGastos = len(gastos)
valorGastos = sum(gastos)
valorCompras = 0

for i in gastos:
    if(i > 3000):
        qtdCompras += 1
        valorCompras += i

pctGastos = (valorCompras /  valorGastos) * 100

print(f"Foram feitas {qtdCompras} compras acima de 3000")
print(f"Porcentagem acima de 3000: {pctGastos}%")