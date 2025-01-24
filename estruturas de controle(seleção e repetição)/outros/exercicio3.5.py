n = int(input("Informe um número inteiro: "))
acumulador=1

for x in range(1,n+1,1):
    acumulador *=x

print(acumulador)
