def arranjo(numero, p):
    total = 1
    total2 = 1
    elemento = numero - p
    if numero > 0:
        for w in range(1, numero + 1,1):
            total *= w

        print()
        for x in range(1 , elemento + 1, 1):
            total2 *= x
    
        elemento = total/total2
        print(f"O total de elementos corresponde ao seguinte valor: {elemento}")
    elif numero == 0:
        return print("Informe um número maior que zero!!!!!!!!!!")

n = int(input("Informe um número inteiro: "))
m = int(input("Informe o tamanho do arranjo: "))

arranjo(n,m)
