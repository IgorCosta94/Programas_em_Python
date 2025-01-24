n = int(input("Forneça um número inteiro: "))

acumulador=0

for x in range(1,n+1,1):
    acumulador = acumulador +(1/x)

print(acumulador)
