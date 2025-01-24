v1 = [0] * 10
v2 = [0] * 10
v3 = [0] * 10

cont = 0

for w in range(0,9,1):
    v1[w] = int(input("Informe um número inteiro V1: "))
    v2[w] = int(input("Informe um número inteiro V2: "))

for x in range(0,9,1):
    for y in range(0,9,1):
        if v1[x] == v2[y]:
            v3[x] = v1[x]

for x in range(0,10,1):
    for y in range(x+1,9,1):
        if v3[x] == v3[y]:
            v3[y] = 0
        
print(f"V1 = {v1}")
print(f"V2 = {v2}")
print(f"V3 = {v3}")
