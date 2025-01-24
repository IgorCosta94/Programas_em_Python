n=int(input("Digite um numero inteiro: "))

contador=1


for x in range(n):
    contador=x*x
    if(contador<=n):
        a=x

print(f"O numero que é ou mais se aproxima da raiz desse numero {n} é: {a}")
