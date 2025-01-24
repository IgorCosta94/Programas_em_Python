v1n = ['0'] * 10
v1L = [0] * 10

v2n = ['0'] * 10
v2L = [0] * 10

v3n = ['0'] * 10
v3L = [0] * 10

for x in range(0,10,1):
   nome = input("Informe o nome do produto: ")
   custo = float(input("Informe o custo do produto: "))
   preco = float(input("Informe o preço do produto: "))

   lucro = preco - custo

   lucro = (((lucro - custo) / preco) * 100)
   if lucro < 10.0:
        v1n[x] = nome
        v1L[x] = lucro
   elif (lucro >= 10.0) and (lucro <= 30.0):
        v2n[x] = nome
        v2L[x] = lucro
   elif lucro > 30.0:
        v3n[x] = nome
        v3L[x] = lucro


for x in range(0,10,1):
    if v1L[x] != 0:
        print(f"Os produto com lucro menor que 10% são:\n   Nome:{v1n[x]}\n  Lucro:{v1L[x]}")

for x in range(0,10,1):
    if v2L[x] != 0:
        print(f"Os produto com lucro entre 10% e 30% são:\n   Nome:{v2n[x]}\n   Lucro:{v2L[x]}")

for x in range(0,10,1):
    if v3L[x] != 0:
        print(f"Os produto com lucro maior que 30% são:\n   Nome:{v3n[x]}\n  Lucro:{v3L[x]}")
