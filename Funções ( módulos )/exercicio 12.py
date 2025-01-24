def divisores(numero):
    print(f"Os divisores de {numero} são: ", end = " ")
    for w in range(1, numero + 1, 1):
        if numero % w == 0:
            print(f"{w}, ", end = " ")
            

n = int(input("Informe um número inteiro: "))

divisores(n)
