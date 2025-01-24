def alfabeto():
    letra = []
    cont = 1
    while cont <= 26:
        letra.append(input("Informe um letra do alfabeto:"))
        cont += 1
    ordem(letra)

def ordem(alfa):
    for w in range(0,len(alfa),1):
        for x in range(w+1, len(alfa), 1):
            comp = alfa[w]
            if alfa[w] > alfa[x]:
                alfa[w] = alfa[x]
                alfa[x] = comp
    print(alfa)

        
alfabeto()
