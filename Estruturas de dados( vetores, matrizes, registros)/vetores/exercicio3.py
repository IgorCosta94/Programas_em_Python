v1 = [0] * 20
v2 = [0] * 20
cont = 0
######################################################################################
for x in range(0,20,1):
    v1[x] = int(input("Informe um número inteiro: "))
######################################################################################
for x in range(0,18,1):
    if v1[x] < v1[x+1]:
        cont += 1
    else:
        v2[x] = cont
        cont = 0
v2[len(v1)-1] = cont
######################################################################################
n = 0
for x in range(0,20,1):
    if v2[x] > n:
        n = v2[x]

print(f"A maior sequencia de números em ordem crescente e de {n}")
