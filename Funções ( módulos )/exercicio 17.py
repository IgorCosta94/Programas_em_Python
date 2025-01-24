def fatorial():
    resultado = 1
    n = int(input("Digite um número inteiro: "))
    if n > 0:
        for w in range(1,n+1,1):
            resultado *= w
    return n,resultado

#a,b=fatorial()
x = fatorial()
print(f"O fatorial de {x[0]} é igual a {x[1]}")
