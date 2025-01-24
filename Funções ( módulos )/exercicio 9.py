def raiz(w):
    cont = 1
    soma = 0
    while cont < w:
        soma +=1
        cont = soma * soma

    if cont == w:
        print(f"A raiz quadrada de {w} é {soma}") 
    elif cont  > w:
        cont  = 0.0
        soma = 0.0
        while cont <= w:
            soma += 0.0000001
            cont = soma * soma
        print(f"O valor mais próximo da raiz quadrada de {w} é {round(soma,6)}") 

n = int(input("Informe o numerador: "))

raiz(n)
