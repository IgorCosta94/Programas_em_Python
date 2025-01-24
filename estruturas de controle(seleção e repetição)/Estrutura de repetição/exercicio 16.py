x1 = int(input("Informe um número inteiro para a base  "))
x2 = int(input("Informe um número inteiro para o expoente "))

acum = 1

for x in range(1,x2+1,1):
    acum *= x1

print(f"\nO número {x1} elevado a {x2} e igual a {acum}")
