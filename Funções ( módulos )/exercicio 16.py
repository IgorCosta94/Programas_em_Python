def absoluto():
    n = int(input("Digite 1 se o número for racional e 2 se for inteiro\n"))
    if n == 1:
        n = float(input("Digite um número racional: "))
        if n < 0:
            return n * -1
        else:
            return n
    elif n == 2:
        n = int(input("Digite um número inteiro: "))
        if n < 0:
            return n * -1
        else:
            return n
    




print(absoluto())
