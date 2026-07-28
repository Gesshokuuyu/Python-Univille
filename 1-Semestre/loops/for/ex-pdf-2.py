#  Escreva um programa para calcular quantos dias levará para a colônia de uma
# bactéria A ultrapassar ou igualar a colônia de uma bactéria B, com base nas taxas
# de crescimento de 3% e 1,5% respectivamente. Considere que a colônia A inicia
# com 4 elementos e a B com 10

colonia_A = 4
colonia_B = 10

taxa_A = 0.03
taxa_B = 0.015

dias = 0

while colonia_B >= colonia_A:
    colonia_A += colonia_A * taxa_A
    colonia_B += colonia_B * taxa_B
    dias += 1

print(f"Demorou {dias} dias para Colonia A ser maior que a Colonia B")
print(f"Colonia A: {colonia_A:.2f}")
print(f"Colonia B: {colonia_B:.2f}")
