def exponenciacao(base, expoente):
    x = base
    for w in range(2, expoente+1,1):
        base *= x
    print(base)

n = int(input("Informe a base do expoente: "))
n2 = int(input("Informe o expoente da base: "))

exponenciacao(n,n2)
