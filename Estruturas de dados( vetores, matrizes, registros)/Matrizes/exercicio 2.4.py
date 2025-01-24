distancia = [[0,0,0,0,0,0,0],
             [0,2,11,6,15,11,1],
             [0,2,7,12,4,2,15],
             [0,11,7,11,8,3,13],
             [0,6,12,11,10,2,1],
             [0,15,4,8,10,5,13],
             [0,11,2,3,2,5,14],
             [0,1,15,13,1,13,14]]

n1 = 1
n2 = 1
acum = 0
while n1 != 0 and n2 != 0:
    n1 = int(input("Informe a primeira cidade: "))
    n2 = int(input("Informe a segunda cidade: "))

    if n1 != n2 and (n1 <=6 and n2 <=6):
        tempo = distancia[n1][n1] + distancia[n2][n2]
        print(tempo)
        acum += tempo
        print(f"O tempo para percorrer as duas cidades foi de {tempo} min")
    else:
        print("INFORME DUAS CIDADES DIFERENTES")


print("O total do percuso foi de: ", acum)
    

viagem = [[0,0],
          [0,0]]
cont = 0
while cont <= 4:
    n1 = int(input("Informe a primeira cidade: "))
    

    if n1 != n2 and (n1 <=6 and n2 <=6):
        for x in range(0,2,1):
            for y in range(0,2,1):
                viagem[x][y] = n1
