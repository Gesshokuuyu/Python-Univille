def printarNaVertical(num):
    if num < 10:
        print(num)
        return
   
    printarNaVertical(num // 10)
    print(num % 10)

    


printarNaVertical(3214123213)