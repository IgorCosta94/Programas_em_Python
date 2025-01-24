v1 = [0] * 10


for x in range(0,10,1):
    v1[x] = int(input("Informe um numero inteiro: "))

v2 = [0] * len(v1)

for x in range((len(v2)-1),-1,-1):
    v2[x] = v1[9-x]

print(v1)
print(v2)
