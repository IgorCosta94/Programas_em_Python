v1 = [0] * 20

for x in range(len(v1)):
    v1[x] = int(input("Digite um número inteiro: "))

for x in range(len(v1)):
    for y in range(x+1,20):
        a = v1[x]

        if a >= v1[y]:
            v1[x] = v1[y]
            v1[y] = a

print(v1)
