v1 = [0] * 10
v2 = [0] * 10
for x in range(0,10,1):
    v1[x] = int(input("Informe um numero inteiro: "))
    if (v1[x] % 2) == 0:
        v2[x] = v1[x] * 2
    elif (v1[x] % 2) == 1:
        v2[x] = v1[x] * 3
        
print(v1)
print(v2)
