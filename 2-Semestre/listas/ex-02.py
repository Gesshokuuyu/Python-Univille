def cumsum(list):
    lastTotal = 0
    for idx, vlr in enumerate(list):
        list[idx] += lastTotal
        lastTotal = list[idx]
    return list

print(cumsum([1, 2, 3]))