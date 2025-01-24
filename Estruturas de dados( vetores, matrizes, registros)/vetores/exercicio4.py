v1 = [0] * 50

media = 0
aci_media = 0.0
abai_media = 0.0
cont_aci = 0
cont_abai = 0

for x in range(0,50,1):
    v1[x] = float(input("Informe a nota: "))
    media += v1[x]

media = media / 50
aci_media = media + (media*0.10)
abai_media = media - (media*0.10)

for x in range(0,50,1):
    if v1[x] > aci_media:
        cont_aci += 1
    elif v1[x] < abai_media:
        cont_abai += 1

print(f"Média: {media}")
print(f"Quantidade de notas 10% acima da média: {cont_aci}")
print(f"Quantidade de notas 10% abaixo da média: {cont_abai}")
