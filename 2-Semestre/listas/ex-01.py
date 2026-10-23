# Escreva uma função chamada nested_sum que receba uma lista de listas de números inteiros e adicione os elementos de todas 
# as listas aninhadas. Por exemplo:

# >>> t = [[1, 2], [3], [4, 5, 6]]
# >>> nested_sum(t)
# 21

def nested_sum(lists):
    total = 0
    for list in lists: 
        total += sum(list)

    return total

print(nested_sum([[1, 4],[5]]))