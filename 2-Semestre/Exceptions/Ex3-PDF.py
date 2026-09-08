#Captura de Exceções Específicas
#Crie uma calculadora simplificada de divisão que solicite dois valores ao usuário e exiba o
#resultado da divisão do primeiro pelo segundo. Trate especificamente os seguintes erros com
#mensagens personalizadas:
#ValueError: Caso o usuário digite algo que não possa ser convertido para número
#(float ou int).
#ZeroDivisionError: Caso o usuário tente dividir por zero.

try:
    d1 = int(input("Informe o dividendo: "))
    d2 = int(input("Informe o divisor: "))
    print(d1/d2)
except ValueError:
    print("Entrada invalida.")
except ZeroDivisionError:
    print("Não é possível dividir um número por 0!")
