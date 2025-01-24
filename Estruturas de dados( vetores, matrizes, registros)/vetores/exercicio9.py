altura =[1.78, 2.20, 1.50, 1.78, 1.33,1.78]
moda = [0] * 6
media = 0
soma = 0
des = 0.0
#Alternatica a)#
for x in range(0,6,1):
    media += altura[x]
    soma += pow(altura[x],2)
#Alternatica b)#
for x in range(0,5,1):
    cont = 1
    for y in range(x+1,6,1):
        if altura[x] == altura[y]:
            cont += 1
    moda[cont] = cont

#Alternatica c)#
n = moda[0]
for x in range(1,5,1):
    if moda[x] > n:
        n = moda[x]
#Alternatica d)#
for x in range(0,5,1):
    for y in range(x+1,6,1):
        mediana = altura[x]
        if altura[x] > altura[y]:
            altura[x] = altura[y]
            altura[y] = mediana

des = pow(media/6,2)
print(f"Média das alturas: {round(media/5,2)}")
print(f"Desvio padrão: {round(((soma/5)- des),3)}")
print(f"Valor da moda: {n}")
print(f"O valor da mediana é: {altura[(len(altura)//2)]}")

