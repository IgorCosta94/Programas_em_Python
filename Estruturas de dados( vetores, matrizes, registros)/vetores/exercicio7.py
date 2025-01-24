v1 = [0] * 10
v2 = [0] * 10
v3 = [0] * 20

cont = 0

for w in range(0,9,1):
    v1[w] = int(input("Informe um número inteiro V1: "))
    v2[w] = int(input("Informe um número inteiro V2: "))

for x in range(0,10,1):
    v3[x] = v1[x]
for y in range(0,10,1):
    v3[10+y] = v2[y]

for x in range(0,20,1):
    for y in range(x+1,19,1):
        if v3[x] == v3[y]:
            v3[y] = 0


for x in range(0,20,1):
    for y in range(x+1,19,1):
        cont = v3[x]
        if v3[x] > v3[y]:
            v3[x] = v3[y]
            v3[y] = cont
        

print(f"V1 = {v1}")
print(f"V2 = {v2}")
print(f"V3 = {v3}")
