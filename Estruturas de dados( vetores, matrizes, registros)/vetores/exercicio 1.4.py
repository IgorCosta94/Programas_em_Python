v1 = [0] * 10
v2 = [0] * 10

cont = 0

while(cont < 10 ):
    n = int(input("Informe um número entre 1 e 5(inclusive)"))
    if n >= 1 and n <= 5:
        v1[cont] = n
        cont += 1
    else:
        print("NÚMERO INCORRETO!! TENTE NOVAMENTE\n")


cont = 1
while(cont <= 5 ):
    cont2 = 0
    for x in range(len(v1)):
        if(v1[x] == cont):
            cont2 += 1
    v2[cont2] = cont2
    cont += 1

print(v2)
